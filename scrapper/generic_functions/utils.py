import os
import pandas as pd

#from scrapper.generic_functions.upload_to_database import flush_data_on_db, load_cases_refs_on_db, load_data_on_db
from upload_to_database import flush_data_on_db, load_cases_refs_on_db, load_data_on_db

directory = './data/'
node_relation_for_csvs = {
    "cases":"legalCases",
    "magistrates":"legalMagistrates",
    "backgrounds":"legalBackgrounds",
    "articles":"legalArticles",
    "headers":"legalHeaders",
    "dictums":"legalDictums",
    "abstracts":"legalAbstracts",
    "fundamentals":"legalFundamentals"
}

flush_node_relation_for_csvs = {
    "cases":"flushLegalCases",
    "magistrates":"flushLegalMagistrates",
    "backgrounds":"flushLegalBackgrounds",
    "articles":"flushLegalArticles",
    "headers":"flushLegalHeaders",
    "dictums":"flushLegalDictums",
    "abstracts":"flushLegalAbstracts",
    "fundamentals":"flushLegalFundamentals"
}

section:str = 'legalData'

method:str = 'POST'

headers = {
  'Content-Type': 'application/json'
}

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def update_case_ref(files):
    for file in files:
        if 'cases' in file:
            df = pd.read_csv(file)
            df_to_json = df.to_json (orient="records")
            load_cases_refs_on_db(section,headers,method,df_to_json)

def get_data_files():
    folder_files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename).replace('\\','/')
        if os.path.isfile(f):
            folder_files.append(f)
    return folder_files


def csv_to_json(files):
    for file in files:
        df = pd.read_csv(file)
        n:int= 200
        list_df = [df[i:i+n] for i in range(0,df.shape[0],n)]
        file_title = file.split('/')[-1].split('.csv')[0]
        endpoint = node_relation_for_csvs[file_title]
        flush_endpoint = flush_node_relation_for_csvs[file_title]
        for chunk in list_df:
            df_to_json = chunk.to_json (orient="records")
            load_data_on_db(section,endpoint,headers,method,df_to_json)
        flush_data_on_db(section,flush_endpoint,headers,method)

files = get_data_files()
update_case_ref(files)
csv_to_json(files)