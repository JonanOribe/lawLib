from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
case_id:str = '29174'
url:str = config['URLS']['SpanishSupremeCourt']+case_id

returned_data = DataScrapper(url).get_data()
print(returned_data)