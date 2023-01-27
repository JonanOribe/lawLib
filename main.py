from typing import List
import json
from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = ['1','2','29174']
url:str = config['URLS']['SpanishSupremeCourt']

returned_data = DataScrapper(url,case_ids).get_data()
print(returned_data)