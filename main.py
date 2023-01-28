from typing import List
from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
case_ids:List = [str(i) for i in [*range(1,5)]]
source:str = 'SpanishSupremeCourt'

#Something like data/json_data.json
output_path:str = config['EXTRA']['OutputPath']

#Get some cases
returned_data = DataScrapper(source,case_ids).get_data()
print(returned_data)

#Save cases as JSON
DataScrapper(source,case_ids).save_data('json',output_path)