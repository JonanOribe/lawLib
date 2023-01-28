import os
import unittest
from scrapper import SupremeCourtUnitedStates
import configparser
from typing import List
import json

config = configparser.ConfigParser()
config.read("config.ini")
area:str = 'courts'
source:str = 'USASupremeCourt'
output_path:str = '{}{}_{}{}'.format(config['EXTRA']['OutputPath'],source,area,'.json')


class SupremeCourtUnitedStatesTestCase(unittest.TestCase):

    def setUp(self):
        self.SupremeCourtUnitedStates = SupremeCourtUnitedStates(source,area)

    def test_get_first_element(self):
        result = self.SupremeCourtUnitedStates.get_data()
        self.assertEqual(result['results'][0]['id'], 'scotus')

    def test_check_json_file(self):
        self.SupremeCourtUnitedStates.save_data('json',output_path)
        try:
            with open(output_path) as json_file:
                data = json.load(json_file)
            if os.path.exists(output_path):
                os.remove(output_path)
        except Exception:
            raise RuntimeError()
        else:
            self.assertGreater(data['count'], 0)

if __name__ == '__main__':
    unittest.main()