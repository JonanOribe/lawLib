from typing import List
from scrapper import SupremeCourtUnitedStates, SupremeCourtSpain
from scrapper.generic_functions.utils import chunks
import configparser
import time
import random

config = configparser.ConfigParser()
config.read("config.ini")

case_ids:List = [str(i) for i in [*range(1,500)]]
area:str='courts'
source_SpanishSupremeCourt:str = 'SpanishSupremeCourt'
source_USASupremeCourt:str = 'USASupremeCourt'

#Something like data/
output_path:str = config['EXTRA']['OutputPath']

#Get some cases and save them on local files
case_ids_chunks = list(chunks(case_ids, 10))
for chunk in case_ids_chunks:
    #SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data(output_path,'json',True)
    SupremeCourtSpain(source_SpanishSupremeCourt,chunk).get_data(output_path,'graph',True)
    delay:int = (250/1000) * random.randint(0, 10)
    print('Waiting for {miliseconds} seconds to avoid blocking from the server'.format(miliseconds = delay))
    time.sleep(delay)

#Get some cases and return as list
#print(SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data(output_path,'json',False))

#Get some cases and save them on local files
#SupremeCourtUnitedStates(source_USASupremeCourt,area).get_data(output_path,'json',True)

#Get some cases and return as list
#print(SupremeCourtUnitedStates(source_USASupremeCourt,area).get_data(output_path,'json',False))

print('The process has ended successfully!!')

