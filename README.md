# TravelCrawl :spider: 

### About The Project
______________________________
```
A web application to retrieve travel fare information scraped from the web. 
```

### Project Structure
______________________________
```
A web application to retrieve travel fare information scraped from the web. 
```
<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Graph That Repo!</title><link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.1.0/css/font-awesome.min.css"><link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet"><link rel="stylesheet" type="text/css" href="/css/main.css"></head><body><div id="colorful-header"></div><div class="main-content"><h1 class="main-header text-center">Input a Github Repository URL</h1><a data-toggle="modal" data-target=".explanation-modal" class="git-style-link explain-app-link">Input a git-what?</a><form id="main-form" method="" action=""><input type="text" name="input" id="input-url" placeholder="Your Repo URL Here" class="repo-input"><button type="submit" class="form-submit">Submit!</button></form></div><div tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel" aria-hidden="true" class="modal fade explanation-modal"><div class="modal-dialog modal-sm"><div class="modal-content"><h2 class="main-modal-header">Need help?</h2><ol><li>Go to <a href="https://github.com/" target="_blank" class="git-style-link">Github</a></li><li>Find an <a href="https://github.com/explore" target="_blank" class="git-style-link">awesome repository</a></li><li>Paste the link and submit!</li></ol><h2 class="modal-header">Still not following?</h2><h4 class="modal-header-ul">Ok! Just click one of these links!</h4><ul class="example-links"><li><a href="https://github.com/jquery/jquery" class="example-repo-link git-style-link">jQuery</a></li><li><a href="https://github.com/twbs/bootstrap" class="example-repo-link git-style-link">Bootstrap</a></li><li><a href="https://github.com/jashkenas/backbone" class="example-repo-link git-style-link">BackboneJS</a></li><li><a href="https://github.com/AndyLampert/repository-file-tree-generator" class="example-repo-link git-style-link">This App's Repo!</a></li></ul></div></div></div><div id="error-container"></div><div id="d3-container"></div></body><script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script><script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script><script src="//cdnjs.cloudflare.com/ajax/libs/d3/3.4.8/d3.min.js"></script><script type="text/javascript" src="js/vendor/d3.layout.js"></script><script type="text/javascript" src="js/main.js"></script></html>


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
$ git clone https://github.com/guergabo/Travel_Fare_Meta_Search_Website
```
```
$ python3 manage.py runsever
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

<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102282323-6a3e1180-3efe-11eb-9c31-197d2c9fdc43.gif">
</p>

### Data Sources
______________________________
Web Crawling:
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


CSV Manipulation: 
###### Downloaded the the original csv file and filtered down to 6000+ airports. Stored this data in the in the db.sqlite3 database as a django model Aiport 
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
The Datbase Schema was created in Django using models.py
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
User Capabilities
```
User has the ability to search for cheap flights based on: 
- Origin Location
- Destination
- Departure Date
- Return Date

This will display a table of flights based on the query and the user has the ability to select a flight and be redirected to 
check out by clicking the "Buy Now" Icon. 

The interactive and presentation technologies used were Django version 3.1.4.
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102281269-9ce70a80-3efc-11eb-8623-3d99633aa659.gif">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102281451-f2bbb280-3efc-11eb-882d-643355de1644.gif">
</p>

### Admin Can
______________________________
```
Create, Read, Update, or Delete the database of 6000+ airports.
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102285180-b8094880-3f03-11eb-986f-3faddf00c26e.png" width="600">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/65991626/102285197-c35c7400-3f03-11eb-9809-45f49e59258d.png" width="600">
</p>

### Contributors
______________________________
Gabriel Guerra
 
