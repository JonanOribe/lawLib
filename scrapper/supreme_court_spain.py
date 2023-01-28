from typing import List
import requests
import json

from scrapper.data_scrapper import DataScrapper

class SupremeCourtSpain(DataScrapper):
    def __init__(self,source:str, case_ids:List[str]):
        super().__init__(source)
        self.case_ids:List = case_ids

    def get_data(self):
      completed_response = []
      for case_id in self.case_ids:
        completed_url:str = self.source+case_id
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", completed_url, headers=headers, data={})

        completed_response.append(response.json())

        if (int(case_id) % 100 == 0):
          print('Number of scrapped elements: '+case_id)

      return completed_response

    def save_data(self, format:str, output_path:str):
      data:List = self.get_data()
      if format == 'json':
        with open(output_path, 'w') as outfile:
          json.dump(data, outfile)