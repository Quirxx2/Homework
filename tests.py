from rss_reader import RssParser
import os
import unittest
from bs4 import BeautifulSoup


class TestParser(unittest.TestCase):

    def setUp(self):

        self.parser = RssParser()

        self.parser.args.source = list()
        self.parser.news_date = '20211030'
        self.parser.args.LIMIT = 3
        self.parser.args.html_path = os.getcwd()

        self.feed = {
            "title": "Feed: 1",
            "description": "Desc",
            "pubDate": "Sat, 30 Oct 2021 06:01:09",
            "items": [
                {
                    "id": 1,
                    "title": "Subtitle 1",
                    "pubDate": "Sat, 30 Oct 2021 02:12:00 GMT",
                    "image": "",
                    "description": "Desc1",
                    "link": "https://www.dw.com/",
                    "content": "100\n",
                    "links": []
                },
                {
                    "id": 2,
                    "title": "Subtitle 2",
                    "pubDate": "Fri, 29 Oct 2021 23:20:00 GMT",
                    "image": "",
                    "description": "Desc2",
                    "link": "https://www.dw.com/",
                    "content": "200\n",
                    "links": []
                }
            ]
        }

    def tearDown(self):
        pass

    def test_to_html(self):

        a = list()
        a.append(self.feed)
        self.parser.convert_to_html(self.parser.args.html_path, a)

        with open(self.parser.args.html_path + 'output.html', 'r') as f1:
            newhtml_content = f1.read()

        with open(os.getcwd() + '\\' + 'demo.html', 'r') as f2:
            oldhtml_content = f2.read()

        self.assertEqual(newhtml_content, oldhtml_content)

    def test_date_conv(self):
        datestr = "Sat, 30 Oct 2021 06:01:09"
        exp_datestr = "20211030"
        act_datestr = self.parser.short_date(datestr)
        self.assertEqual(act_datestr, exp_datestr)

    def test_name_conv(self):
        namestr = "10"
        exp_namestr = "d3d9446802a44259755d38e6d163e820"
        act_namestr = self.parser.hash_name(namestr)
        self.assertEqual(act_namestr, exp_namestr)

    def test_news_cash(self):
        act_newscash = self.parser.news_cashing()
        print(act_newscash)
        self.assertEqual(act_newscash[0], self.feed)

    def test_content_from_html(self):
        url = 'https://news.yahoo.com/33-old-california-man-says-145448113.html'
        desc = ''
        res_str = '''A 33-year-old California man was able to pay off his student loan debt after committing to eating nearly all his meals at Six Flags for seven years.\u00a0\nThe man identified as Dylan started to take advantage of Six Flags Magic Mountain's annual pass in 2014 when he was working as an intern in an office minutes away from the amusement park, WKRC reported.\u00a0\n\"You can pay around $150 for unlimited, year-round access to Six Flags, which includes parking and two meals a day,\" Dylan said in an interview with Mel Magazine. \"If you time it right, you could eat both lunch and dinner there every day.\"\u00a0\nDuring the first year, Dylan admitted that he doesn't think he \"ever went to the grocery store\" and acknowledged that the theme park menu, which was made up of burgers, fries, and pizza, \"wasn't healthy at all, which was rough\" the outlet reported.\u00a0\nSince then, in addition to paying off his student loans, Dylan was able to buy a house and get married, according to reports. The exact amount of his student loan debt wasn't reported.\u00a0\nHe estimates that he has eaten over 2,000 meals at the amusement park over the years, paying about 50 cents for each meal, Mel Magazine reported.\u00a0\nAfter getting married, Dylan said he stopped eating at Six Flags for dinner and on the weekends. However, he still goes to enjoy at least three lunches during the week.\u00a0\n\"We just bought a house here, so I'm not really going anywhere,\" Dylan told Mel Magazine. \"As long as they keep changing the menu, I'm happy.\"\n\u00a0\nRead the original article on Insider\n'''

        t = self.parser.get_content_from_html(url, desc)
        self.assertEqual(t, res_str)

    def test_read_rss_from_url(self):
        self.parser.args.source.append('https://news.yahoo.com/rss/')
        exp_res_t = 'Feed: ' + 'Yahoo News - Latest News & Headlines'
        t = self.parser.read_rss_from_url()
        self.assertEqual(t['title'], exp_res_t)

    def test_split_desc(self):
        test_str = '<p>Своей находкой ребята поделились в Facebook, пишет издание <a href="https://www.dailystar.co.uk/news/weird-news/couple-find-mystery-secret-room-25308268" target="_blank">Daily Star</a>.</p>'
        res_str = 'Своей находкой ребята поделились в Facebook, пишет издание Daily Star.'
        dc = BeautifulSoup(test_str, features="html.parser")
        t = self.parser.split_desc(dc)
        self.assertEqual(t['desc_text'], res_str)


if __name__ == '__main__':
    unittest.main()
