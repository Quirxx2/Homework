import json
import re
import argparse
import sys
import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class RssParser:
    def __init__(self):

        # Configuring parser arguments
        parser = argparse.ArgumentParser(prog="rss_reader.py", description='Pure Python command-line RSS reader.')
        parser.add_argument('source', nargs='*', default=None, help="RSS URL")
        parser.add_argument('--version', action="version", version="RSS parser ver. 1.0",
                            help="Print version info")
        parser.add_argument('--json', action="store_true", help="Print result as JSON in stdout")
        parser.add_argument('--verbose', action="store_true", help="Outputs verbose status messages")
        parser.add_argument('--limit', dest='LIMIT', default=-1, type=int,
                            help='Limit news topics if this parameter provided')
        self.args = parser.parse_args()

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

        soup_page = BeautifulSoup(response_page.text, 'lxml')

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
            logging.info(f'RSS channel description name "{desc_tag.text}" was detected')
            desc = desc_tag.text
        except AttributeError:
            logging.info('RSS channel description name was not detected')
            desc = ''
        try:
            date_tag = soup.find('channel').find('pubDate')
            logging.info(f'RSS channel date "{date_tag.text}" was detected')
            datepub = date_tag.text
        except AttributeError:
            logging.info('RSS channel description name was not detected')
            datepub = ''
        if datepub == '':
            try:
                date_tag = soup.find('channel').find('lastBuildDate')
                logging.info(f'RSS channel date "{date_tag.text}" was detected')
                datepub = date_tag.text
            except AttributeError:
                logging.warning('RSS channel description name was not detected. Using current date and time')
                datepub = datetime.now().strftime("%a, %d %B %Y %I:%M:%S") + " MSK"
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
                    if pubdate == "":
                        pubdate = "" if items[i].lastBuildDate is None else items[i].lastBuildDate.text

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


if __name__ == '__main__':

    rss = RssParser()

    rss_news = rss.read_rss_from_url()

    logging.info('Printing information')

    if rss.args.json:
        rss.print_to_stdout_as_json(rss_news)
    else:
        rss.print_to_stdout(rss_news)

    logging.info("Program finished successfully")
