from typing import List
from scrapper import SupremeCourtUnitedStates, SupremeCourtSpain
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

case_ids:List = [str(i) for i in [*range(1,5)]]
area:str='courts'
source_SpanishSupremeCourt:str = 'SpanishSupremeCourt'
source_USASupremeCourt:str = 'USASupremeCourt'

#Something like data/
output_path:str = config['EXTRA']['OutputPath']

#Get some cases and save them on local files
print(SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data(output_path,'json',True))

#Get some cases and return as list
print(SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data(output_path,'json',True))

#Get some cases
#print(SupremeCourtUnitedStates(source_USASupremeCourt,area).get_data())

#SupremeCourtUnitedStates(source_USASupremeCourt,area).save_data('json',output_path)

