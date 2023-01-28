import unittest
from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
source:str = 'SpanishSupremeCourt'


class DataScrapperTestCase(unittest.TestCase):

    def setUp(self):
        self.DataScrapper = DataScrapper(source)

    def test_get_valid_url(self):
        object_source:str = self.DataScrapper.source
        valid_url:str = config['URLS'][source.lower()]
        self.assertEqual(object_source, valid_url)

if __name__ == '__main__':
    unittest.main()