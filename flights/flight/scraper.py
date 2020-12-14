# File: data_sources.py
# Description: This file accesses, formats, and merges travel fare data with covid19 data.
# Name: Gabriel Guerra
# Uniqname: Guergabo
# Date-Modified: 12-06-2020


'''
NOTES:
Does not make sense to cache flight info because of how quickly flight information changes. | immediately ?
'''


### PACKAGES ###
import requests                                      # python package for GET request.
import json                                          # python package for converting json format.
from bs4 import BeautifulSoup                        # python package for scraping HTML.
import pandas as pd                                  # python package for dataFrames.
import re                                            # python package for finding strings.


### COLUMNS FOR DATAFRAME ###
out_airlines = []                                    # create list for outbound airline.
in_airlines = []                                     # create list for inbound airline.
out_dep_times = []                                   # create list for outbound departure times.
in_dep_times = []                                    # create list for inbound departure times.
out_arr_times = []                                   # create list for outbound arrival times.
in_arr_times = []                                    # create list for inbound arrival times.
out_stops = []                                       # create list for outbound stops.
in_stops = []                                        # create list for inbound stops.
out_durations = []                                   # create list for outbound duration.
in_durations = []                                    # create list for inbound duration.
prices = []                                          # create list for flight prices.
check_out_urls = []                                  # create a list for the check out url of the other websites.


### KAYAK URL ###
def kayak_url_structure(dep_loc, des_loc, dep_date, ret_date=None):
    '''
    This function returns proper Kayak.com URL based
    on query parameters.

    :parameter
    -----------
    dep_loc: departure location of the flight.
    des_loc: destination location of the flight.
    dep_date: departure date of the flight.
    ret_date: return date of the flight, default=None (one-way).

    :returns
    -----------
    Correct url structure with a search query for Kayak.
    '''
    # URL STRUCTURE.
    BASE_URL = 'https://www.kayak.com/flights/'                             # base url.

    # LOCATIONS.
    FROM_LOC = dep_loc                                                      # departure location.
    TO_LOC = des_loc                                                        # destination location.
    FLIGHT_PATH = f'{FROM_LOC}-{TO_LOC}/'                                   # flight path formatting.

    # DATES.
    DEPARTURE_DATE = f'{dep_date}/'                                         # departure date.
    RETURN_DATE = f'{ret_date}'                                             # arrival date.
    DATE_PATH = DEPARTURE_DATE + RETURN_DATE                                # date path formatting.

    # PARAMETERS.
    PARAMETERS = '?sort=bestflight_a'                                       # sorting parameters.

    # TYPES.
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
    url: kayak url with an active search.

    :returns
    -----------
    df: pandas dataframe of the url page.

    '''
    # REQUEST HTML.
    headers = {                                                           # get around being detected as a bot.
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    URL = url                                                             # url describing origin, destination, start and end date.
    page_response = requests.get(URL, headers=headers)                    # request data from the browser.
    HTML = page_response.text                                             # convert to HTML text.
    soup = BeautifulSoup(HTML, 'html.parser')                             # create instance to parse HTML.
    search_list = soup.find('div', id='searchResultsList')                # find the parent class.

    # AIRLINES x 2 | ROUND-TRIP.
    airlines = search_list.find_all('div', class_='section times')        # find all of the classes with airline name.
    count = 1
    for airline in airlines:                                              # parse the list.
        al = airline.find('div', class_='bottom')                         # pick out the specific nested class with info.
        if count % 2 == 1:                                                # outbound airlines are the odd ones (1,3,5).
            out_airlines.append(al.contents[0].strip())
        else:                                                             # inbound airlines are the even ones (2,4,6).
            in_airlines.append(al.contents[0].strip())
        count += 1

    # DEPARTURE TIMES x 2 | ROUND-TRIP.
    times = search_list.find_all('span', class_='depart-time base-time')  # find all the classes containing departure times.
    count = 1
    for span in times:                                                    # parse the list.
        if count % 2 == 1:                                                # outbound departure times are the odd ones (1,3,5).
            out_dep_times.append(span.string.strip())
        else:                                                             # inbound departure times are teh even ones (2,4,6).
            in_dep_times.append(span.string.strip())
        count += 1

    # ARRIVAL TIMES X 2 | ROUND-TRIP.
    arr_times = search_list.find_all('span', class_= 'arrival-time base-time')  # find all the classes containing arrival times
    count = 1
    for span in arr_times:                                                      # parse the list.
        if count % 2 == 1:  # it is reverse on the html structure               # outbound departure times are the odd ones (1,3,5).
            out_arr_times.append(span.string.strip())
        else:                                                                   # inbound departure times are teh even ones (2,4,6).
            in_arr_times.append(span.string.strip())
        count += 1

    # STOPS X 2 | ROUND-TRIP.
    stops = search_list.find_all('span', class_='stops-text')                   # find all the classes containing stops.
    count = 1
    for stop in stops:                                                          # parse the list.
        if count % 2 == 1:                                                      # outbound stops are the odd ones (1,3,5).
            out_stops.append(stop.contents[0].strip())
        else:                                                                   # inbound stops are the even ones (2,4,6).
            in_stops.append(stop.contents[0].strip())
        count += 1

    # DURATIONS x 2 | ROUND-TRIP.
    durations = search_list.find_all('div', class_='section duration allow-multi-modal-icons')     # find all the classes containing durations.
    count = 1
    for duration in durations:                                                                     # pare the list.
        dur = duration.find('div', class_='top')                                                   # find the specific nested class.
        if count % 2 == 1:                                                                         # outbound duration are the odd ones (1,3,5).
            out_durations.append(dur.contents[0].strip())
        else:                                                                                      # inbound duration are the even ones (2,4,6).
            in_durations.append(dur.contents[0].strip())
        count  += 1

    # PRICES | ROUND-TRIP.
    regex = re.compile('Common-Booking-MultiBookProvider (.*)multi-row Theme-featured-large(.*)')  #
    price_list = search_list.find_all('div', class_=regex)                                         #
    for pr in price_list:                                                                          # parse the list.
        price = pr.find('span', class_='price-text')                                               # find the nested class with price.
        prices.append(price.contents[0].strip())                                                   # append price to prices.

    # CHECK OUT URL/REDIRECTING
    '''
        if check_out_url == javascript:void(0) ... do something !
    '''
    check_out_list = search_list.find_all('div', class_='col col-best')                            # find all the classes containing check out urls.
    for cl in check_out_list:                                                                      # parse the list.
        check_out_url = cl.find('a')['href']                                                       # find the nested url.
        full_url = 'https://www.kayak.com' + check_out_url                                         # concatenate to base url.
        check_out_urls.append(full_url)                                                            # append url to list.

    # CREATE DATA FRAME.
    df = df_create(url)     # create data frame.
    return df


### CREATE DATA FRAME ###
def df_create(url):
    '''
    This function creates a dataFrame using the
    data scraped from kayak.com and the covid19 API data.

    :parameter
    -----------
    url: kayak url with an active search.

    :returns
    -----------
    df: pandas dataframe of the scraped data.
    '''
    # PARSE THROUGH THE URL TO GET INFO.
    url_list = url.split('/')                    # split the url.
    route_split = url_list[4].split('-')         # split the routes.
    end_split = url_list[6].split('?')           # split the parameter.

    # ASSIGN INFORMATION.
    origin = route_split[0]                      # assign origin from url.
    destination = route_split[1]                 # assign destination from url.
    startdate = url_list[5]                      # assign startdate from url.
    enddate = end_split[0]                       # assign enddate from url.

    # CREATE DATA FRAME | array must be same length == NA?
    data = {
        'origin': origin,                        # origin location of the flight.
        'destination': destination,              # destination location of the flight.
        'startdate': startdate,                  # start date of the flight.
        'enddate': enddate,                      # end date of the flight.
        'out_airlines': out_airlines,            # outbound flight airline.
        'in_airlines': in_airlines,              # inbound flight airline.
        'out_dep_times': out_dep_times,          # outbound departure time.
        'in_dep_times': in_dep_times,            # inbound departure time.
        'out_arr_times': out_arr_times,          # outbound departure time.
        'in_arr_times': in_arr_times,            # inbound departure time.
        'out_stops': out_stops,                  # outbound stop.
        'in_stops': in_stops,                    # inbound stop.
        'out_durations': out_durations,          # outbound duration.
        'in_durations': in_durations,            # inbound duration.
        'prices': prices,                        # flight price.
        'check_out': check_out_urls              # check out url.
    }
    df = pd.DataFrame.from_dict(data)

    return df                                    # returning the pandas dataframe.


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
    # GET IATA CODE FROM CITY NAMES.
    outbound = (air.iata_retrieve('DETROIT')).upper()
    inbound =  (air.iata_retrieve('MIAMI')).upper()

    # GET DEPARTURE AND RETURN DATES.
    # ... [through django?]

    # CREATE URL.
    url = kayak_url_structure(outbound, inbound, '2021-02-07', '2021-02-12')
    print(url)

    # GET FLIGHT INFORMATION.
    kayak_scraping(url)

