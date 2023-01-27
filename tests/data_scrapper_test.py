import unittest
from scrapper import DataScrapper
import configparser
from typing import List

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = ['1','2','29174']
url:str = config['URLS']['SpanishSupremeCourt']


class DataScrapperTestCase(unittest.TestCase):

    def setUp(self):
        self.DataScrapper = DataScrapper(url,case_ids)

    def test_get_first_element(self):
        result = self.DataScrapper.get_data()
        self.assertEqual(result[0]["ID"], int(case_ids[0]))

    def test_count_elements(self):
        result = self.DataScrapper.get_data()
        self.assertEqual(len(result), len(case_ids))


if __name__ == '__main__':
    unittest.main()