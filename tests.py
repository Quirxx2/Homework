from rss_reader import RssParser
import os
import unittest


class RssNews(RssParser):

    def __init__(self, limit):
        self.args.source = None
        self.news_date = '20211030'
        self.args.LIMIT = limit
        self.args.html_path = os.getcwd()


class TestParser(unittest.TestCase):

    def __init__(self):
        super().__init__()

        self.limit = 3
        self.parser = RssNews(self.limit)
        self.feed = [{
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
                },
            ]
        }]

        self.res = '''
    <body>
    <main>

            <h1>Feed: 1</h1>
            <h1>Sat, 30 Oct 2021 06:01:09</h1>

                <h2>Desc</h2>



                        <h2>Subtitle 1</h2>


                        <h2>Sat, 30 Oct 2021 02:12:00 GMT</h2>


                        <h3>Desc1</h3>


                        <p><a href="https://www.dw.com/">https://www.dw.com/</a></p>


                        <p>100
    </p>






                        <h2>Subtitle 2</h2>


                        <h2>Fri, 29 Oct 2021 23:20:00 GMT</h2>


                        <h3>Desc2</h3>


                        <p><a href="https://www.dw.com/">https://www.dw.com/</a></p>


                        <p>200
    </p>






    </main>
    </body>
    </html>'''

    def test_to_html(self):

        self.parser.convert_to_html(self.parser.args.html_path, self.feed)

        with open(self.parser.args.html_path + 'output.html', 'r') as f:
            html_content = f.read()

        index = html_content.find('<body>')
        html_data = html_content[index:]

        self.assertEqual(html_data, self.res)

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
        self.assertEqual(act_newscash, self.feed)


if __name__ == '__main__':
    unittest.main()
