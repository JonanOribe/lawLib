from typing import List
import requests
import json
import pandas as pd
from os.path import exists
from scrapper.data_scrapper import DataScrapper

class SupremeCourtSpain(DataScrapper):
    def __init__(self,source:str, case_ids:List[str]):
        super().__init__(source)
        self.case_ids:List = case_ids
        self.already_merge = {
            "cases":False,
            "magistrates":False,
            "backgrounds":False,
            "articles":False,
            "headers":False,
            "dictums":False,
            "abstracts":False,
            "fundamentals":False
          }

    def prepare_csv(self,output_path:str):
      files_and_elements:List[str]={
            "cases":self.cases,
            "magistrates":self.magistrates,
            "backgrounds":self.backgrounds,
            "articles":self.articles,
            "headers":self.headers,
            "dictums":self.dictums,
            "abstracts":self.abstracts,
            "fundamentals":self.fundamentals
          }
      for key, value in files_and_elements.items():
        self.data_saver(output_path,key,value)

    def csv_checker(self,path:str,file_name:str,new_dataframe):
      full_path:str = path+file_name+'.csv'
      new_dataframe_formatted = pd.DataFrame.from_records(new_dataframe)
      if (self.already_merge[file_name] != True and exists(full_path)):
        current_file = pd.read_csv(full_path)
        self.already_merge[file_name]=True
        return pd.concat([current_file,new_dataframe_formatted])
      return new_dataframe_formatted

    def data_saver(self,output_path:str,file_name:str, values):
      values_json = json.loads(json.dumps([ob.__dict__ for ob in values]))
      full_values_json = self.csv_checker(output_path,file_name,values_json)
      full_values_json.to_csv(output_path+file_name+'.csv',index=False)

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