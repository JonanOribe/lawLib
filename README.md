# lawLib

Library to extract legal information from official resources.

### Installation
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

### Get started
Get data from Spanish Supreme Court:

```Python
from typing import List
from scrapper import DataScrapper

case_ids:List = [str(i) for i in [*range(1,5)]]
source:str = 'SpanishSupremeCourt'

output_path:str = 'data/json_data.json'

#Get some cases
returned_data = DataScrapper(source,case_ids).get_data()
print(returned_data)

#Save cases as JSON
DataScrapper(source,case_ids).save_data('json',output_path)
```