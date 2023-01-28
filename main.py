from typing import List
from scrapper import SupremeCourtUnitedStates, SupremeCourtSpain
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

case_ids:List = [str(i) for i in [*range(1,5)]]
area:str='courts'
source_SpanishSupremeCourt:str = 'SpanishSupremeCourt'
source_USASupremeCourt:str = 'USASupremeCourt'

#Something like data/SpanishSupremeCourt.json
output_path_SpanishSupremeCourt:str = '{}{}{}'.format(config['EXTRA']['OutputPath'],source_SpanishSupremeCourt,'.json')
output_path_USASupremeCourt:str = '{}{}_{}{}'.format(config['EXTRA']['OutputPath'],source_USASupremeCourt,area,'.json')

#Get some cases
print(SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data())

#Save cases as JSON
SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).save_data('json',output_path_SpanishSupremeCourt)

#Get some cases
print(SupremeCourtUnitedStates(source_USASupremeCourt,area).get_data())

SupremeCourtUnitedStates(source_USASupremeCourt,area).save_data('json',output_path_USASupremeCourt)

