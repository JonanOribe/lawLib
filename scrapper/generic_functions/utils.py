import os
import pandas as pd

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def get_data_files():
    directory = './data/'
    folder_files = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename).replace('\\','/')
        # checking if it is a file
        if os.path.isfile(f):
            folder_files.append(f)
    return folder_files

def csv_to_json(files):
    for file in files:
        df = pd.read_csv (file)
        df.to_json (file.split('.csv')[0]+'.json',orient="records")

files = get_data_files()
csv_to_json(files)