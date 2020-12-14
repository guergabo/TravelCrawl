# File: covid19.py
# Description: This file accesses covid19 data from the rapid API.
# Name: Gabriel Guerra
# Uniqname: Guergabo
# Date-Modified: 12-12-2020


### PACKAGES ###
import requests
import airports as air

### COVID19 API ###
def covid_api():
    '''
    This function makes GET request to the
    Covid19 API to retrieve case count data.

    :parameter
    -----------

    :returns
    -----------

    '''
    # API URL.
    url = "https://covid-19-statistics.p.rapidapi.com/reports"

    # PARAMETERS.
    # print(destination)
    # IATA_DICT = air.build_airport_dictionary()
    # IATA = IATA_DICT[destination]
    # print(IATA)

    COUNTRY = 'USA'
    querystring = {"iso": COUNTRY, "date": "2020-10-16"}

    # HEADERS.
    headers = {
        'x-rapidapi-key': "73ba7d9f54msh86ba0850821a4e9p18ab4bjsnb5eed4d09373",
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

    # REQUEST DATA.
    response = requests.request("GET", url, headers=headers, params=querystring)
    python_dict = response.json()

    # GET CONFIRMED CASES.
    confirmed = python_dict['data'][0]['confirmed']
    return confirmed

if __name__ == '__main__':
    covid_api('Detroit')