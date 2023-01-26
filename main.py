from scrapper import DataScrapper
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
url:str = config['URLS']['SpanishSupremeCourt']+'29174'

returned_data = DataScrapper(url).get_data()
print(returned_data)