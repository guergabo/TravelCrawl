# File: data_sources.py
# Description: This file accesses, formats, and merges travel fare data with covid19 data.
# Name: Gabriel Guerra
# Uniqname: Guergabo
# Date-Modified: 12-06-2020

### PACKAGES ###
import requests                                      # python package for GET request.
import json                                          # python package for converting json format.
from bs4 import BeautifulSoup                        # python package for scraping HTML.
import pandas as pd                                  # python package for dataFrames.
import re


### KAYAK URL ###
def kayak_url_structure(dep_loc, des_loc, dep_date, ret_date=None):
    '''
    This function returns proper Kayak.com URL based
    on query parameters.

    :parameter
    -----------

    :returns
    -----------

    '''
    # URL Structure
    BASE_URL = 'https://www.kayak.com/flights/'                             # base url.

    FROM_LOC = dep_loc                                                      # departure location.
    TO_LOC = des_loc                                                        # destination location.
    FLIGHT_PATH = f'{FROM_LOC}-{TO_LOC}/'                                   # flight path formatting.

    DEPARTURE_DATE = f'{dep_date}/'                                         # departure date.
    RETURN_DATE = f'{ret_date}'                                             # arrival date.
    DATE_PATH = DEPARTURE_DATE + RETURN_DATE                                # date path formatting.

    PARAMETERS = '?sort=bestflight_a'                                       # sorting parameters.

    ROUND_TRIP_URL = BASE_URL + FLIGHT_PATH + DATE_PATH + PARAMETERS        # url for round-trip flights.
    ONE_WAY_URL = BASE_URL + FLIGHT_PATH + DEPARTURE_DATE + PARAMETERS      # url for one-way flights.

    if ret_date is None:                                                    # determine one-way or round-trip.
        return ONE_WAY_URL                                                  # return one-way trips.
    return ROUND_TRIP_URL                                                   # return two-way trips.


### KAYAK WEB SCRAPING ###
def kayak_scraping(url):
    '''
    This function scrapes the HTML from Kayak.com
    and parses through the travel fare data.

    :parameter
    -----------

    :returns
    -----------

    '''
    headers = { # get around being detected as a bot.
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    URL = url                                              # url describing origin, destination, start and end date.
    page_response = requests.get(URL, headers=headers)     # request data from the browser.
    HTML = page_response.text                              # convert to HTML text.
    soup = BeautifulSoup(HTML, 'html.parser')              # create instance to parse HTML.


    # AIRLINE x 2 | ROUND-TRIP
    dep_airlines = []
    ret_airlines = []
    search_list = soup.find('div', id='searchResultsList')
    airlines = search_list.find_all('div', class_='section times')
    count = 1
    for airline in airlines:
        al = airline.find('div', class_='bottom')
        if count % 2 == 1:
            dep_airlines.append(al.contents[0].strip())
        else:
            ret_airlines.append(al.contents[0].strip())
        count += 1
    print('departure airlines:', dep_airlines)
    print('return airlines:', ret_airlines)


    # DEPARTURE TIME x 2 | ROUND-TRIP
    dep_times = []
    ret_times = []
    search_list = soup.find('div', id='searchResultsList')
    times = search_list.find_all('span', class_='depart-time base-time')
    count = 0
    for span in times:
        if count % 2 == 1: # it is reverse on the html structure
            ret_times.append(span.string.strip())
        else:
            dep_times.append(span.string.strip())
        count += 1
    print('departure times:', dep_times)
    print('return times:', ret_times)


    # ARRIVAL TIME X 2 | ROUND-TRIP
    arr_dest_time = []
    arr_ret_time = []
    search_list = soup.find('div', id='searchResultsList')
    arr_times = search_list.find_all('span', class_= 'arrival-time base-time')
    count = 0
    for span in arr_times:
        if count % 2 == 1:  # it is reverse on the html structure
            arr_ret_time.append(span.string.strip())
        else:
            arr_dest_time.append(span.string.strip())
        count += 1
    print('Arrival-to times:', arr_dest_time)
    print('Arrival-from times:', arr_ret_time)

    # STOPS X 2 | ROUND-TRIP
    stop_out = []
    stop_in = []
    search_list = soup.find('div', id='searchResultsList')
    stops = search_list.find_all('span', class_='stops-text')
    count = 0
    for stop in stops:
        if count % 2 == 1:
            stop_out.append(stop.contents[0].strip())
        else:
            stop_in.append(stop.contents[0].strip())
        count += 1
    print('stop out:', stop_out)                      ### check with international etc!!!
    print('stop in:',stop_in)

    # DURATION x 2 | ROUND-TRIP
    duration_out = []
    duration_in = []
    search_list = soup.find('div', id='searchResultsList')
    durations = search_list.find_all('div', class_='section duration allow-multi-modal-icons')
    count = 0
    for duration in durations:
        dur = duration.find('div', class_='top')
        if count % 2 == 1:
            duration_in.append(dur.contents[0].strip())
        else:
            duration_out.append(dur.contents[0].strip())
        count  += 1
    print('duration out:', duration_out)
    print('duration in:', duration_in)

    # PRICE || domestic need new expression for international?
    price_list = []
    search_list = soup.find('div', id='searchResultsList')
    regex = re.compile('Common-Booking-MultiBookProvider (.*)multi-row Theme-featured-large(.*)')
    prices = search_list.find_all('div', class_=regex)
    for pr in prices:
        price = pr.find('span', class_='price-text')
        price_list.append(price.contents[0].strip())
    print('Price:', price_list)

### COVID19 API ###
def covid_api(destination):
    '''
    This function makes GET request to the
    Covid19 API to retrieve case count data.

    :parameter
    -----------

    :returns
    -----------

    '''
    BASE_URL = 'https://api.covid19api.com/'               # base url for api.
    API_KEY = '5cf9dfd5-3449-485e-b5ae-70a60e997864'       # api key required.
    params = {'apiKey':API_KEY}                            # parameters for query.
    json_response = requests.get(BASE_URL, params=params)  # request data from the server.
    python_response = json_response.json()                 # convert the json response into python obj.
    print(python_response)                                 # print the python obj.


### MERGE DATA ###
def df_create(source):
    '''
    This function creates a dataFrame using the
    data from kayak.com and the covid19 API data.

    :parameter
    -----------

    :returns
    -----------

    '''
    pass
    dep_airline = airlines
    ret_airline = airlines

    # origin =
    # destination =
    # dep_date =
    # ret_date =

    price = prices
    # dep_time_o =
    # arr_time_d =
    # duration_to =
    # stops_to =

    # dep_time_d =
    # arr_time_o =
    # duration_from =
    # stops_from =

    covid_count = covid_api(destination)

    df = pd.DataFrame({
        'airline': airline,
        'origin': origin,
        'destination': destination,
        'dep_date': dep_date,
        'ret_date': ret_date,
        'price': price,
        'currency': 'USD',
        'dep_time_org': dep_time_org,
        'arr_time_des': arr_time_des,
        'duration_to': duration_to,
        'stops_to': stops_to,
        'dep_time_des': dep_time_des,
        'arr_time_org': arr_time_org,
        'duration_from': duration_from,
        'stops_from': stops_from,
        'covid_count': covid_count,
    })




### CACHE DATA ### || USE THE URL AS A KEY IN THE DICTIONARY !
def data_cache(source):
    '''
    This function stores any responses into a
    json file to later retrieve from.

    :parameter
    -----------

    :returns
    -----------

    '''
    pass



if __name__ == '__main__':
    # initial URL tests
    url = kayak_url_structure('DTT', 'LAX', '2021-02-07', '2021-02-12')
    print(url)
    kayak_scraping(url)


