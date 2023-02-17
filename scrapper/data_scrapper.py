import configparser
from typing import List
import pandas as pd
import json
from models.article import Article
from models.background import Background
from models.dictum import Dictum
from models.header import Header

from models.magistrate import Magistrate

config = configparser.ConfigParser()
config.read("config.ini")

class DataScrapper:
    def __init__(self, source) -> None:
        self.source:str = {section: dict(config.items(section)) for section in config.sections()}['URLS'][source.lower()]
        self.magistrates:list[Magistrate] = []
        self.backgrounds:list[Background] = []
        self.articles:list[Article] = []
        self.headers:list[Header] = []
        self.dictums:list[Dictum] = []

    def get_scrapper_sources(self):
        return {section: dict(config.items(section)) for section in config.sections()}['URLS']

    def _save_data(self, file_name:str, data, format:str, output_path:str):
      if format == 'json':
        formatted_output_path:str = '{}{}.{}'.format(output_path, file_name, format)
        with open(formatted_output_path, 'w') as outfile:
          json.dump(data, outfile)
      if format == 'graph': 
        case_ref = data['REFERENCIA_BOE']
        for elem in data['RESOLUCIONES_MAGISTRADOS']:
          self.magistrates.append(Magistrate(case_ref,elem))
        for elem in data['RESOLUCIONES_ANTECEDENTES']:
          self.backgrounds.append(Background(case_ref,elem))
        for elem in data['RESOLUCIONES_ARTICULOS']:
          self.articles.append(Article(case_ref,elem))
        for elem in data['RESOLUCIONES_CABECERA']:
          self.headers.append(Header(case_ref,elem))
        for elem in data['RESOLUCIONES_DICTAMEN']:
          self.dictums.append(Dictum(case_ref,elem))