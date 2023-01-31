import configparser
import json

config = configparser.ConfigParser()
config.read("config.ini")

class DataScrapper:
    def __init__(self, source) -> None:
        self.source:str = {section: dict(config.items(section)) for section in config.sections()}['URLS'][source.lower()]

    def get_scrapper_sources(self):
        return {section: dict(config.items(section)) for section in config.sections()}['URLS']

    def _save_data(self, file_name:str, data, format:str, output_path:str):
      if format == 'json':
        formatted_output_path:str = '{}{}.{}'.format(output_path, file_name, format)
        with open(formatted_output_path, 'w') as outfile:
          json.dump(data, outfile)