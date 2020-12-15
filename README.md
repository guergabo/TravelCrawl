# TravelCrawl :spider: 

### About The Project
A web application to retrieve travel fare information scraped from the web. 

### Built With
```
- HTML5
- CSS3
- Python  
- Django Web FrameWork
```

### Getting Started
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
##### Web Crawling:
###### Requested and parsed through the HTML. No caching was used because of how often the data changes (seconds).
```
URL: https://www.kayak.com/flight
Format: HTML
```
##### CSV Manipulation: 
###### Downloaded the the original csv file and filtered down to 6000+ airports. Stored this data in the in the db.sqlite3 database as a django model Aiport 
```
URL: https://openflights.org/data.html#airport
Format: CSV
```

### Database
```

```

### Interaction 
```

```

### Web Users Can
```

```

### Admin Can
```

```

### Contributers
Gabriel Guerra
 
