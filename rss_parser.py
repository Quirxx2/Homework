import json
import re
import argparse
import sys
import logging
from datetime import datetime
import hashlib
import os

import requests
from bs4 import BeautifulSoup


class RssParser:
    def __init__(self):

        # Configuring parser arguments
        parser = argparse.ArgumentParser(prog="rss_reader.py",
                                         description='Pure Python command-line RSS reader.')
        parser.add_argument('source', nargs='*', default=None, help="RSS URL")
        parser.add_argument('--version', action="version", version="RSS parser ver. 3.0",
                            help="Print version info")
        parser.add_argument('--json', action="store_true", help="Print result as JSON in stdout")
        parser.add_argument('--verbose', action="store_true", help="Outputs verbose status messages")
        parser.add_argument('--limit', dest='LIMIT', default=-1, type=int,
                            help='Limit news topics if this parameter provided')
        parser.add_argument('--date',
                            dest='news_date',
                            help="Save RSS in a local storage",
                            type=lambda data_s: datetime.strptime(data_s, '%Y%m%d'))

        self.args = parser.parse_args()

        if self.args.news_date is not None:
            nd = self.args.news_date.timetuple()
            self.news_date = str(nd[0]) + str(nd[1]) + str(nd[2])
        else:
            self.news_date = ''

        if (self.args.LIMIT is not None) and (self.args.LIMIT < 1) and (self.args.LIMIT != -1):
            print('Wrong --limit argument will be set to default value')
            self.args.LIMIT = -1

        # Setting up logging level
        if self.args.verbose is True:
            logging.basicConfig(level=logging.DEBUG,
                                format="%(levelname)s: %(asctime)s - %(message)s",
                                datefmt="%d.%m.%Y %H:%M:%S")
        else:
            logging.basicConfig(level=logging.ERROR,
                                format="%(levelname)s: %(message)s")

    @staticmethod
    def get_content_from_html(url):
        # Requesting html data
        try:
            response_page = requests.get(url)
            response_page.raise_for_status()
            logging.info('HTML data has been downloaded successfully')
        except Exception as e:
            logging.error(f'Download failed with {e}')
            sys.exit(1)

        soup_page = BeautifulSoup(response_page.text, 'html.parser')

        # Finding very long string in p-tags
        p_nodes = soup_page.findAll('p')
        item_page = []
        for p_node in p_nodes:
            if p_node.parent.name == 'div':
                max_words = 0
                temp_text = p_node.text + '\n'
                item_page.append(temp_text)
                other_nodes = p_node.next_siblings
                for other_node in other_nodes:
                    if other_node.name == 'p':
                        temp_text = other_node.text + '\n'
                        item_page.append(temp_text)
                for item in item_page:
                    max_words = max_words + len(re.findall(r'\w+', item))
                if max_words > 30:
                    logging.info('HTML text has been found')
                    return ''.join(item_page)
        logging.info('HTML text has not been found')
        return ''

    def read_rss_from_url(self):
        # Requesting RSS data
        try:
            response = requests.get(self.args.source[0])
            response.raise_for_status()
            logging.info('RSS feed has been downloaded successfully')
        except Exception as e:
            logging.error(f'Download failed with {e}')
            sys.exit(1)

        # Processing RSS data into dictionary
        soup = BeautifulSoup(response.text, features='xml')
        # Head
        news = dict()
        try:
            if soup.find('channel') is None:
                logging.info(f'RSS channel was detected')
        except AttributeError:
            logging.error('Channel was not found in the document')
            sys.exit(1)
        try:
            title_tag = soup.find('channel').find('title')
            logging.info(f'RSS channel title name "{title_tag.text}" was detected')
            title = 'Feed: ' + title_tag.text
        except AttributeError:
            logging.info('RSS channel title name was not detected')
            title = ''
        try:
            desc_tag = soup.find('channel').find('description')
            logging.info(f'RSS channel description name "{desc_tag.tetx}" was detected')
            desc = desc_tag.text
        except AttributeError:
            logging.info('RSS channel description name was not detected')
            desc = ''
        try:
            date_tag = soup.find('channel').find('pubDate')
            logging.info(f'RSS channel date "{date_tag.text}" was detected')
            datepub = date_tag.text
            # Removing timezone info
            i_pub = datepub.rfind(' ')
            datepub = datepub[:i_pub]
        except AttributeError:
            logging.info('RSS channel description name was not detected')
            datepub = ''
        if datepub == '':
            try:
                date_tag = soup.find('channel').find('lastBuildDate')
                logging.info(f'RSS channel date "{date_tag.text}" was detected')
                datepub = date_tag.text
                # Removing timezone info
                i_pub = datepub.rfind(' ')
                datepub = datepub[:i_pub]
            except AttributeError:
                logging.warning('RSS channel description name was not detected. Using current date and time')
                datepub = datetime.now().strftime("%a, %d %B %Y %I:%M:%S")
        logging.info(f'{datepub} is pubDate')
        news['channel'] = {'title': title, 'description': desc, 'pubDate': datepub}
        # Tail
        i = -1
        try:
            items = soup.findAll('item')
            for i in range(len(items)):
                if (self.args.LIMIT != -1) and ((i + 1) > self.args.LIMIT):
                    logging.info('Finishing fetching')
                    break
                else:
                    title = "" if items[i].title is None else items[i].title.text
                    desc = "" if items[i].description is None else items[i].description.text
                    link = "" if items[i].link is None else items[i].link.text
                    pubdate = "" if items[i].pubDate is None else items[i].pubDate.text
                    image_x = items[i].find("media:content", attrs={"url": True})
                    image = "" if image_x is None else image_x['url']
                    # if there is a link to outer page it needs to open and grab a content
                    if link != '':
                        content = self.get_content_from_html(link)
                    else:
                        content = ''
                news[f'news {i + 1}'] = {"title": title,
                                         "pubDate": pubdate,
                                         "image": image,
                                         "description": desc,
                                         "link": link,
                                         "content": content}
                logging.info(f'{i + 1} news have been fetched')
            return news
        except Exception as e:
            logging.warning(f'Something went wrong. Only {i + 1} news have been found. {e} occured')
            return None

    @staticmethod
    def print_to_stdout(rss_data):
        logging.info('Formatting data to plain text')
        print(rss_data['channel']['title'])
        if rss_data['channel']['description']:
            print(rss_data['channel']['description'])
        print()
        for item in rss_data:
            if item.startswith('news'):
                link_count = 1
                if rss_data[item]['title'] != '':
                    print(f"Title: {rss_data[item]['title']}")
                if rss_data[item]['description'] != '':
                    print(f"Description: {rss_data[item]['description']}")
                if rss_data[item]['link'] != '':
                    print(f"Link: {rss_data[item]['link']}")
                if rss_data[item]['pubDate'] != '':
                    print(f"Date: {rss_data[item]['pubDate']}")
                print()
                if rss_data[item]['content'] != '':
                    print(rss_data[item]['content'])
                print('\nLinks:')
                if rss_data[item]['link'] != '':
                    print(f"[{link_count}]: {rss_data[item]['link']} (link)")
                    link_count += 1
                if rss_data[item]['image'] != '':
                    print(f"[{link_count}]: {rss_data[item]['image']} (image)")
                print()

    @staticmethod
    def print_to_stdout_as_json(rss_data):
        json_data = json.dumps(rss_data, ensure_ascii=False, indent=4, default=str)
        logging.info('RSS data has been converted to JSON object')
        print(json_data)

    @staticmethod
    def short_date(date_string):
        try:
            logging.info(f'{date_string} is a parsed pubDate')
            ds = datetime.strptime(date_string, "%a, %d %b %Y %I:%M:%S")
            tds = ds.timetuple()
        except ValueError:
            ds = datetime.strptime(date_string, "%a, %d %B %Y %I:%M:%S")
            tds = ds.timetuple()
        logging.info(f'Head of file name is {str(tds[0]) + str(tds[1]) + str(tds[2])}')
        return str(tds[0]) + str(tds[1]) + str(tds[2])

    @staticmethod
    def hash_name(rss_name):
        rss_hash = hashlib.md5(rss_name.encode())
        return rss_hash.hexdigest()

    @staticmethod
    def read_from_json(f_desc):
        try:
            logging.info(f'Reading information from {f_desc}')
            data = json.load(f_desc)
        except Exception:
            raise FileNotFoundError('Could not read json file. Not file or file is empty.')
        return data

    @staticmethod
    def write_to_json(f_desc, data):
        logging.info(f'Starting writing in the file {f_desc}')
        json.dump(data, f_desc, indent=4)
        logging.info(f'Ending writing in the file {f_desc}')

    def news_cashing(self):

        c_body = []

        if (len(self.args.source) == 0) and (self.news_date != ''):
            # There is no file specified, only date. Just fetch ALL news from a local storage by date
            # LIMIT parameter impacts on every file individually
            path = os.getcwd()
            index = 0
            f_data = dict()
            with os.scandir(path) as listOfEntries:
                for entry in listOfEntries:
                    if entry.is_file():
                        file_date = entry.name[:8]
                        # Scanning all files with the same date
                        if file_date == self.news_date:
                            index += 1
                            with open(entry.name, 'r', encoding='utf-8') as f:
                                f_data[index] = self.read_from_json(f)
                                # Truncating data to LIMIT
                                if (f_data[index] is not None) \
                                        and (self.args.LIMIT != -1) \
                                        and (self.args.LIMIT < (len(f_data[index]) - 1)):
                                    for key in range(self.args.LIMIT + 1, len(f_data[index])):
                                        del f_data[index][f'news {key}']
                                c_body.append(f_data[index])
            return c_body

        elif (len(self.args.source) != 0) and (self.news_date != ''):
            # There are a source of data and date. Fetch news from a local storage by source and date
            logging.info('Creating file name')
            file_head = self.news_date
            file_tail = self.hash_name(self.args.source[0])
            file_body = file_head + ' ' + file_tail + '.json'
            with open(file_body, 'r', encoding='utf-8') as f:
                f_data = self.read_from_json(f)
            # Truncating data to LIMIT
            if (f_data is not None) \
                    and (self.args.LIMIT != -1) \
                    and (self.args.LIMIT < (len(f_data) - 1)):
                for key in range(self.args.LIMIT + 1, len(f_data)):
                    del f_data[f'news {key}']
            c_body.append(f_data)
            return c_body

        elif len(self.args.source) != 0:
            # There is only a source of data. Fetch news from the source and put them to a local storage
            # As well make them available to print
            rss_news = self.read_rss_from_url()
            file_head = self.short_date(rss_news['channel']['pubDate'])
            file_tail = self.hash_name(self.args.source[0])
            file_body = file_head + ' ' + file_tail + '.json'
            # Updating file with news if exists. Old data will be erased. Otherwise creating new one
            with open(file_body, 'w', encoding='utf-8') as f:
                self.write_to_json(f, rss_news)
            c_body.append(rss_news)
            return c_body


if __name__ == '__main__':

    rss = RssParser()

    logging.info('Cashing information')

    cashed_news = rss.news_cashing()

    if cashed_news is None:
        raise Exception('News were not found')

    logging.info('Printing information')

    for news in cashed_news:
        if rss.args.json:
            rss.print_to_stdout_as_json(news)
        else:
            rss.print_to_stdout(news)

    logging.info("Program finished successfully")
