from typing import List
from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = ['1','2','29174']
url:str = config['URLS']['SpanishSupremeCourt']
output_path:str = config['EXTRA']['OutputPath']

#Get some cases
returned_data = DataScrapper(url,case_ids).save_data('json')
print(returned_data)

#Save cases as JSON
DataScrapper(url,case_ids).save_data('json',output_path)