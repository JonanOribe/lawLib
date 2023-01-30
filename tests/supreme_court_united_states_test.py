import os
import unittest
from scrapper import SupremeCourtUnitedStates
import configparser
import glob

config = configparser.ConfigParser()
config.read("config.ini")
area:str = 'courts'
source:str = 'USASupremeCourt'
output_path:str = config['EXTRA']['OutputPath']


class SupremeCourtUnitedStatesTestCase(unittest.TestCase):

    def setUp(self):
        self.SupremeCourtUnitedStates = SupremeCourtUnitedStates(source,area)

    def test_get_areas(self):
        options = self.SupremeCourtUnitedStates.get_areas()
        self.assertGreater(len([key for key in options.keys()]),1)

    def test_get_first_element(self):
        result = self.SupremeCourtUnitedStates.get_data(output_path,'json',False)
        self.assertEqual(result['results'][0]['id'], 'scotus')

    def test_check_json_file(self):
        response = self.SupremeCourtUnitedStates.get_data(output_path,'json',True)
        try:
            if os.path.exists(output_path):
                files = glob.glob(output_path+'/*.*')
                created_files_count = len(files)
                for f in files:
                    os.remove(f)
        except Exception:
            raise RuntimeError()
        else:
            self.assertNotEqual(created_files_count,0) and self.assertEqual(len(files), 0)
            self.assertIn('Data was saved!',response)

if __name__ == '__main__':
    unittest.main()