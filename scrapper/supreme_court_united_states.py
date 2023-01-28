import requests
from typing import List
import json
from scrapper.data_scrapper import DataScrapper

class SupremeCourtUnitedStates(DataScrapper):
    def __init__(self,source:str, area:str):
        super().__init__(source)
        self.area:str = area

    def get_data(self):
        completed_url:str = self.source+self.area
        headers = {
          'Content-Type': 'application/json'
        }   
        response = requests.request("GET", completed_url, headers=headers, data={}) 
        return response.json()

    def save_data(self, format:str, output_path:str):
      data:List = self.get_data()
      if format == 'json':
        with open(output_path, 'w') as outfile:
          json.dump(data, outfile)