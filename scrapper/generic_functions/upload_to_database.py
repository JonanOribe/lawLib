import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

databaseUrl:str = config['DEFAULT']['databaseUrl']

def load_data_on_db(section,endpoint,headers,method,payload):

    url = "{databaseUrl}{section}/{endpoint}".format(databaseUrl=databaseUrl,section=section,endpoint=endpoint)
    
    print('Current endpoint: {url}'.format(url=url))
    
    response = requests.request(method,url, headers=headers, data=payload)

    print(response.text)

#load_data_on_db(section,endpoint,headers,method,payload)