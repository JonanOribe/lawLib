import os
import unittest
from scrapper import SupremeCourtSpain
import configparser
from typing import List
import glob

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = ['1','2','29174']
source:str = 'SpanishSupremeCourt'
output_path:str = config['EXTRA']['OutputPath']


class SupremeCourtSpainTestCase(unittest.TestCase):

    def setUp(self):
        self.SupremeCourtSpain = SupremeCourtSpain(source,case_ids)

    def test_get_first_element(self):
        result = self.SupremeCourtSpain.get_data(output_path,'json',False)
        self.assertEqual(result[0]["ID"], int(case_ids[0]))

    def test_count_elements(self):
        result = self.SupremeCourtSpain.get_data(output_path,'json',False)
        self.assertEqual(len(result), len(case_ids))

    def test_check_json_file(self):
        response = self.SupremeCourtSpain.get_data(output_path,'json',True)
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