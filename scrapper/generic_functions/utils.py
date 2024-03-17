import os
import pandas as pd
directory = './data/'
node_relation_for_csvs = {
    "cases":"LegalCases",
    "magistrates":"LegalMagistrates",
    "backgrounds":"LegalBackgrounds",
    "articles":"LegalArticles",
    "headers":"LegalHeaders",
    "dictums":"LegalDictums",
    "abstracts":"LegalAbstracts",
    "fundamentals":"LegalFundamentals"
}

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def get_data_files():
    folder_files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename).replace('\\','/')
        # checking if it is a file
        if os.path.isfile(f):
            folder_files.append(f)
    return folder_files

def csv_to_json(files):
    for file in files:
        df = pd.read_csv(file)
        file_title = file.split('/')[-1].split('.csv')[0]
        formatted_file_title = node_relation_for_csvs[file_title]
        df.to_json (directory+formatted_file_title +'.json',orient="records")

files = get_data_files()
csv_to_json(files)