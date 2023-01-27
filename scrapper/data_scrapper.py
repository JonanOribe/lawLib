from typing import List
import requests

class DataScrapper:
    def __init__(self, url, case_ids) -> None:
        self.url:str = url
        self.case_ids:List = case_ids

    def get_data(self):
      completed_response = []
      for case_id in self.case_ids:
        completed_url:str = self.url+case_id
        payload={}
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", completed_url, headers=headers, data=payload)

        completed_response.append(response.json())
      return completed_response

    def save_data(self,begin:int,end:int,format:str):
      pass