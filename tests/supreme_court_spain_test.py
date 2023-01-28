import os
import unittest
from scrapper import SupremeCourtSpain
import configparser
from typing import List
import json

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = ['1','2','29174']
source:str = 'SpanishSupremeCourt'
output_path:str = '{}{}{}'.format(config['EXTRA']['OutputPath'],source,'.json')


class SupremeCourtSpainTestCase(unittest.TestCase):

    def setUp(self):
        self.SupremeCourtSpain = SupremeCourtSpain(source,case_ids)

    def test_get_first_element(self):
        result = self.SupremeCourtSpain.get_data()
        self.assertEqual(result[0]["ID"], int(case_ids[0]))

    def test_count_elements(self):
        result = self.SupremeCourtSpain.get_data()
        self.assertEqual(len(result), len(case_ids))

    def test_check_json_file(self):
        self.SupremeCourtSpain.save_data('json',output_path)
        try:
            with open(output_path) as json_file:
                data = json.load(json_file)
            if os.path.exists(output_path):
                os.remove(output_path)
        except Exception:
            raise RuntimeError()
        else:
            self.assertEqual(len(data), len(case_ids))

if __name__ == '__main__':
    unittest.main()