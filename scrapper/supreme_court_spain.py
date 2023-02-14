from typing import List
import requests
import json
import pandas as pd
from scrapper.data_scrapper import DataScrapper

class SupremeCourtSpain(DataScrapper):
    def __init__(self,source:str, case_ids:List[str]):
        super().__init__(source)
        self.case_ids:List = case_ids

    def prepare_csv(self,output_path:str):
      magistrates_json = json.loads(json.dumps([ob.__dict__ for ob in self.magistrates]))
      pd.DataFrame.from_records(magistrates_json).to_csv(output_path+'magistrados.csv',index=False)
      backgrounds_json = json.loads(json.dumps([ob.__dict__ for ob in self.backgrounds]))
      pd.DataFrame.from_records(backgrounds_json).to_csv(output_path+'backgrounds.csv',index=False)

    def get_data(self, output_path:str, format:str='json', save_data_on_file:bool=False):
      completed_response = []
      for index,case_id in enumerate(self.case_ids):
        completed_url:str = self.source+case_id
        headers = {
          'Content-Type': 'application/json'
        }

        response = requests.request("GET", completed_url, headers=headers, data={}).json()

        if(save_data_on_file):
          super()._save_data(response['REFERENCIA_BOE'], response, format, output_path)
        else:
          completed_response.append(response)

        if (int(index) % 100 == 0):
          print('Number of scrapped elements: '+case_id)

      if(format == 'graph'):
        self.prepare_csv(output_path)

      return completed_response if len(completed_response)>0 else 'Data was saved! on {}'.format(output_path)