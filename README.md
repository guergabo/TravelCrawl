# TravelCrawl :spider: 

### About The Project
______________________________
A web application to retrieve travel fare information scraped from the web. 

### Built With
______________________________
```
- HTML5
- CSS3
- Python  
- Django Web FrameWork
```

### Getting Started
______________________________
Running the Django Application:
```
python3 manage.py runsever
```

Required Packages:
```                                     
from bs4 import BeautifulSoup  # python package                       
import pandas as pd            # python package                                  
import re                      # python package
import json                    # python package
import requests                # python package
import csv                     # python package   
```

![4qhw0e](https://im7.ezgif.com/tmp/ezgif-7-99e760d479a8.gif)


### Data Sources
______________________________
##### Web Crawling:
###### Requested and parsed through the HTML. No caching was used because of how often the data changes (seconds). The scraped data was temporarilty stored in a Pandas DataFrame to take advantage of the functionality to_html() offers.
```
URL: https://www.kayak.com/flight
Format: HTML
```

##### Summary of Scraped Data:
```
data_series = {
    'origin': pd.Series(origin),                        # origin location of the flight.
    'destination': pd.Series(destination),              # destination location of the flight.
    'startdate': pd.Series(startdate),                  # start date of the flight.
    'enddate': pd.Series(enddate),                      # end date of the flight.
    'out_airlines': pd.Series(out_airlines),            # outbound flight airline.
    'in_airlines': pd.Series(in_airlines),              # inbound flight airline.
    'out_dep_times': pd.Series(out_dep_times),          # outbound departure time.
    'in_dep_times': pd.Series(in_dep_times),            # inbound departure time.
    'out_arr_times': pd.Series(out_arr_times),          # outbound departure time.
    'in_arr_times': pd.Series(in_arr_times),            # inbound departure time.
    'out_stops': pd.Series(out_stops),                  # outbound stop.
    'in_stops': pd.Series(in_stops),                    # inbound stop.
    'out_durations': pd.Series(out_durations),          # outbound duration.
    'in_durations': pd.Series(in_durations),            # inbound duration.
    'prices': pd.Series(prices),                        # flight price.
    'check_out': pd.Series(check_out_urls)              # check out url.
}
df = pd.DataFrame(data_series)
```

##### CSV Manipulation: 
###### Downloaded the the original csv file and filtered down to 6000+ airports. Stored this data in the in the db.sqlite3 database as a django model Aiport 
```
URL: https://openflights.org/data.html#airport
Format: CSV
```
###### Summary of Database Data
![Screenshot (1007)](https://user-images.githubusercontent.com/65991626/102278955-a1112900-3ef8-11eb-8b3d-c747b53416f3.png)


### Database
______________________________
###### The Datbase Schema was created in Django using models.py
```
from django.db import models  

# Airport Class for the search bar 
class Airport(models.Model):
    city_name = models.CharField(max_length=250)
    country_name = models.CharField(max_length=250)
    iata_code = models.CharField(max_length=3)

    def __str__(self):
        text = f"{self.city_name}, {self.country_name}, {self.iata_code}"
        return text
```

### Interaction 
______________________________
```

```

### Web Users Can
______________________________
Look up round-trip flight tickets based on 4 categories:
```
- Origin Location
- Destination
- Departure Date
- Return Date
```

### Admin Can
______________________________
```

```

### Contributers
______________________________
Gabriel Guerra
 
