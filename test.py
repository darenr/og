import unittest
import feedparser
import nose.tools

from og import ExtractShareTags

class TestStringMethods(unittest.TestCase):

    _og = ExtractShareTags()


    def test_url_blog(self):
        url="https://blog.insightdatascience.com/the-unreasonable-effectiveness-of-deep-learning-representations-4ce83fc663cf"
        result = self._og.get_share_tags(url)
        self.assertTrue(len(result.keys())>5)

    def test_pypi(self):
        url="https://pypi.org/project/summary-extraction/"
        result = self._og.get_share_tags(url)
        self.assertTrue(len(result.keys())>5)

    def test_rss(self):
        urls = [
            "http://rss.cnn.com/rss/cnn_tech.rss",
            "http://feeds.reuters.com/reuters/technologyNews"
        ]

        for rss in urls:
            d = feedparser.parse(rss)
            for post in d.entries:
                result = self._og.get_share_tags(post.link)
                self.assertTrue(len(result.keys())>5)



if __name__ == '__main__':
    unittest.main()
