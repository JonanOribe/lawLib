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
      cases_json = json.loads(json.dumps([ob.__dict__ for ob in self.cases]))
      full_cases_json = self.csv_checker(output_path,'cases',cases_json)
      full_cases_json.to_csv(output_path+'cases.csv',index=False)

      magistrates_json = json.loads(json.dumps([ob.__dict__ for ob in self.magistrates]))
      magistrates_json = self.csv_checker(output_path,'magistrates',magistrates_json)
      magistrates_json.to_csv(output_path+'magistrates.csv',index=False)

      backgrounds_json = json.loads(json.dumps([ob.__dict__ for ob in self.backgrounds]))
      backgrounds_json = self.csv_checker(output_path,'backgrounds',backgrounds_json)
      backgrounds_json.to_csv(output_path+'backgrounds.csv',index=False)

      articles_json = json.loads(json.dumps([ob.__dict__ for ob in self.articles]))
      articles_json = self.csv_checker(output_path,'articles',articles_json)
      articles_json.to_csv(output_path+'articles.csv',index=False)

      headers_json = json.loads(json.dumps([ob.__dict__ for ob in self.headers]))
      headers_json = self.csv_checker(output_path,'headers',headers_json)
      headers_json.to_csv(output_path+'headers.csv',index=False)

      dictums_json = json.loads(json.dumps([ob.__dict__ for ob in self.dictums]))
      dictums_json = self.csv_checker(output_path,'dictums',dictums_json)
      dictums_json.to_csv(output_path+'dictums.csv',index=False)

      abstracts_json = json.loads(json.dumps([ob.__dict__ for ob in self.abstracts]))
      abstracts_json = self.csv_checker(output_path,'abstracts',abstracts_json)
      abstracts_json.to_csv(output_path+'abstracts.csv',index=False)

      fundamentals_json = json.loads(json.dumps([ob.__dict__ for ob in self.fundamentals]))
      fundamentals_json = self.csv_checker(output_path,'fundamentals',fundamentals_json)
      fundamentals_json.to_csv(output_path+'fundamentals.csv',index=False)

    def csv_checker(self,path:str,file_name:str,new_dataframe):
      full_path:str = path+file_name+'.csv'
      new_dataframe_formatted = pd.DataFrame.from_records(new_dataframe)
      if (self.already_merge[file_name] != True and exists(full_path)):
        current_file = pd.read_csv(full_path)
        self.already_merge[file_name]=True
        return pd.concat([current_file,new_dataframe_formatted])
      return new_dataframe_formatted

      


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