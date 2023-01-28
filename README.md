# lawLib

Library to extract legal information from official resources.

### Get started
Get data from Spanish Supreme Court:

```Python
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
```

### Installation for development purposes
```
<h3>:construction: Working enviroment:</h3>
<li>Python version <b>3.9</b></li> 
<li>Virtual enviroment: <b>py -m venv env</b></li> 
<li>Activate on WINDOWS: <b>env\Scripts\activate</b></li>
<li>Activate on MAC: <b>source env/bin/activate</b></li>
<h3>:books: Dependencies</h3>
<li>Install with: <b>pip3 install -r requirements.txt</b></li>
<h3>:mag_right: Testing</h3>
<li>Launch tests with: <b>python -m unittest -v tests/data_scrapper_test.py</b></li>
```