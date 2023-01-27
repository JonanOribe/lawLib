import os
import unittest
from scrapper import DataScrapper
import configparser
from typing import List
import json

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = ['1','2','29174']
url:str = config['URLS']['SpanishSupremeCourt']
output_path:str = config['EXTRA']['OutputPath']


class DataScrapperTestCase(unittest.TestCase):

    def setUp(self):
        self.DataScrapper = DataScrapper(url,case_ids)

    def test_get_first_element(self):
        result = self.DataScrapper.get_data()
        self.assertEqual(result[0]["ID"], int(case_ids[0]))

    def test_count_elements(self):
        result = self.DataScrapper.get_data()
        self.assertEqual(len(result), len(case_ids))

    def test_check_json_file(self):
        self.DataScrapper.save_data('json',output_path)
        with open(output_path) as json_file:
            data = json.load(json_file)
            if os.path.exists(output_path):
                os.remove(output_path)
        self.assertEqual(len(data), len(case_ids))

if __name__ == '__main__':
    unittest.main()