import requests
from typing import List
import json
from scrapper.data_scrapper import DataScrapper

class SupremeCourtUnitedStates(DataScrapper):
    def __init__(self,source:str, area:str):
        super().__init__(source)
        self.area:str = area

    def get_data(self, output_path:str, format:str='json', save_data_on_file:bool=False):
        completed_url:str = self.source+self.area
        headers = {
          'Content-Type': 'application/json'
        }   

        response = requests.request("GET", completed_url, headers=headers, data={}).json()

        if(save_data_on_file):
          self.__save_data(self.area, response, format, output_path)

        return 'Data was saved! on {}'.format(output_path) if save_data_on_file else response

    def __save_data(self, file_name:str, data,format:str, output_path:str):
      if format == 'json':
        formatted_output_path:str = '{}{}.{}'.format(output_path, file_name, format)
        with open(formatted_output_path, 'w') as outfile:
          json.dump(data, outfile)