import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

log_text:str = 'Current endpoint: '
databaseUrl:str = config['DEFAULT']['databaseUrl']

def load_cases_refs_on_db(section,headers,method,payload):
    url = "{databaseUrl}{section}/{endpoint}".format(databaseUrl=databaseUrl,section=section,endpoint='uploadCasesRefs')
    
    print('{log_text} {url}'.format(log_text=log_text,url=url))
    
    requests.request(method,url, headers=headers, data=payload)

def load_data_on_db(section,endpoint,headers,method,payload):

    url = "{databaseUrl}{section}/{endpoint}".format(databaseUrl=databaseUrl,section=section,endpoint=endpoint)
    
    print('{log_text} {url}'.format(log_text=log_text,url=url))
    
    requests.request(method,url, headers=headers, data=payload)

def flush_data_on_db(section,endpoint,headers,method):

    url = "{databaseUrl}{section}/{endpoint}".format(databaseUrl=databaseUrl,section=section,endpoint=endpoint)
    
    print('{log_text} {url}'.format(log_text=log_text,url=url))
    
    requests.request(method,url, headers=headers, data={})