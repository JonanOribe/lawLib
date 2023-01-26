import unittest
from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
id:int = 29174
url:str = config['URLS']['SpanishSupremeCourt']+str(id)


class DataScrapperTestCase(unittest.TestCase):

    def setUp(self):
        self.DataScrapper = DataScrapper(url)

    def test_zero(self):
        result = self.DataScrapper.get_data()
        self.assertEqual(result["ID"], id)


if __name__ == '__main__':
    unittest.main()