from typing import List
from scrapper import SupremeCourtUnitedStates
import configparser

from scrapper.supreme_court_spain import SupremeCourtSpain

config = configparser.ConfigParser()
config.read("config.ini")

case_ids:List = [str(i) for i in [*range(1,5)]]
area:str='courts'
source_SpanishSupremeCourt:str = 'SpanishSupremeCourt'
source_USASupremeCourt:str = 'USASupremeCourt'

#Something like data/json_data.json
output_path_SpanishSupremeCourt:str = '{}{}{}'.format(config['EXTRA']['OutputPath'],source_SpanishSupremeCourt,'.json')
output_path_USASupremeCourt:str = '{}{}_{}{}'.format(config['EXTRA']['OutputPath'],source_USASupremeCourt,area,'.json')

#Get some cases
returned_data = SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data()
print(returned_data)

#Save cases as JSON
SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).save_data('json',output_path_SpanishSupremeCourt)

#Get some cases
returned_data = SupremeCourtUnitedStates(source_USASupremeCourt,area).get_data()
print(returned_data)

SupremeCourtUnitedStates(source_USASupremeCourt,area).save_data('json',output_path_USASupremeCourt)

