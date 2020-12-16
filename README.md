# TravelCrawl :spider: 

### About The Project
______________________________
A meta search web application for travel fare data. 

### Table of Contents
______________________________
- <a href="https://github.com/guergabo/TravelCrawl#structure">Structure</a>
- <a href="https://github.com/guergabo/TravelCrawl#built-with">Built With</a>
- <a href="https://github.com/guergabo/TravelCrawl#getting-started">Getting Started</a>
- <a href="https://github.com/guergabo/TravelCrawl#data-sources">Data Sources</a>
- <a href="https://github.com/guergabo/TravelCrawl#database">Database</a>
- <a href="https://github.com/guergabo/TravelCrawl#demo">Demo</a>
- <a href="https://github.com/guergabo/TravelCrawl#admin">Admin</a>
- <a href="https://github.com/guergabo/TravelCrawl#contributors">Contributor</a>


### Structure
______________________________
![Screenshot (1010)](https://user-images.githubusercontent.com/65991626/102286230-dec87e80-3f05-11eb-85e1-cdb5987e2af2.png)


### Built With
______________________________
- HTML5
- CSS3
- Python  
- Django Web FrameWork


### Getting Started
______________________________
Required Packages:
- from bs4 import BeautifulSoup                        
- import pandas as pd                                             
- import re                   
- import json                   
- import requests                
- import csv 

```
pip3 install Django
```
```
$ git clone https://github.com/guergabo/Travel_Fare_Meta_Search_Website
```
```
$ python3 manage.py runsever
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102282323-6a3e1180-3efe-11eb-9c31-197d2c9fdc43.gif">
</p>

### Data Sources
______________________________
##### Web Crawling:
Requested and parsed through the HTML. No caching was used because of how often the data changes (seconds). The scraped data was temporarilty stored in a Pandas DataFrame to take advantage of the functionality to_html() offers.
```
URL: https://www.kayak.com/flight
Format: HTML
```

###### Summary of Scraped Data
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
Downloaded the the original csv file and filtered down to 6000+ airports. Stored this data in the db.sqlite3 database as a django model representation. 
```
URL: https://openflights.org/data.html#airport
Format: CSV
```
###### Summary of Database Data
<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102278955-a1112900-3ef8-11eb-8b3d-c747b53416f3.png">
</p>

### Database
______________________________
The Database Schema was created in Django using a script that parsed through iata_db.csv and created instances of the Airport class from models.py.
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

### Demo 
______________________________
User Capabilities
```
User has the ability to search for cheap flights based on: 
- Origin Location
- Destination
- Departure Date
- Return Date

This will display a table of flights based on the query and the user has the ability to select a flight 
and be redirected to check out by clicking the "Buy Now" Icon. 

The interactive and presentation technologies used were Django version 3.1.4.
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102281269-9ce70a80-3efc-11eb-8623-3d99633aa659.gif">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102281451-f2bbb280-3efc-11eb-882d-643355de1644.gif">
</p>

### Admin 
______________________________
```
$ python3 manage.py createsuperuser 
```
```
Can create, read, update, or delete the database of 6000+ airports.
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102285197-c35c7400-3f03-11eb-9809-45f49e59258d.png" width="600">
</p>

### Contributors
______________________________
Gabriel Guerra
- Tree Repository Generator: https://github.com/AndyLampert/repository-file-tree-generator
 
