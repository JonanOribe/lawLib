from typing import List
import unittest
from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
source:str = 'SpanishSupremeCourt'


class DataScrapperTestCase(unittest.TestCase):

    def setUp(self):
        self.DataScrapper = DataScrapper(source)

    def test_get_scrapper_sources_counter(self):
        self.assertEqual(len(self.DataScrapper.get_scrapper_sources()),2)

    def test_get_scrapper_sources_options(self):
        options:List = self.DataScrapper.get_scrapper_sources()
        self.assertEqual([key for key in options.keys()][0],source.lower())

    def test_get_valid_url(self):
        object_source:str = self.DataScrapper.source
        valid_url:str = config['URLS'][source.lower()]
        self.assertEqual(object_source, valid_url)

if __name__ == '__main__':
    unittest.main()