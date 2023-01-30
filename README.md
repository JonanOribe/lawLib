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

#Something like data/
output_path:str = config['EXTRA']['OutputPath']

#Get some cases and save them on local files
SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data(output_path,'json',True)

#Get some cases and return as list
print(SupremeCourtSpain(source_SpanishSupremeCourt,case_ids).get_data(output_path,'json',False))

#Get some cases and save them on local files
SupremeCourtUnitedStates(source_USASupremeCourt,area).get_data(output_path,'json',True)

#Get some cases and return as list
print(SupremeCourtUnitedStates(source_USASupremeCourt,area).get_data(output_path,'json',False))
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