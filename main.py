from typing import List
import json
from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = ['1','2','29174']
url:str = config['URLS']['SpanishSupremeCourt']
output_path:str = config['EXTRA']['OutputPath']

#returned_data = DataScrapper(url,case_ids).save_data('json')
#print(returned_data)

DataScrapper(url,case_ids).save_data('json',output_path)