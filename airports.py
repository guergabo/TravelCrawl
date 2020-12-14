# File: airports.py
# Description: This file create a airports.json that maps city name to airport.
# Name: Gabriel Guerra
# Uniqname: Guergabo
# Date-Modified: 12-06-2020


### PACKAGES ###
import csv                                                              # python package to read csv files.
import json                                                             # python package to write json files.


### IATA AIRPORT CODES ###
IATA_airport_code = dict()                                              # create dictionary.
CACHE_FILENAME = 'airports_iata.json'                                   # file where IATA code data is stored.


### CLEAN AIRPORT.CSV ###
def build_airport_dictionary():
    '''
    This function open the airports.csv
    and cleanly converts the results into
    a dictionary.

    :parameter
    -----------

    :returns
    -----------

    '''
    with open('airports.csv', encoding='utf-8', mode='r') as csv_file:  # open airports.csv from openflights.org
        csv_reader = csv.reader(csv_file, delimiter=',')                # create an instance to be able to parse
        for row in csv_reader:                                          # loop over the rows in the csv.
            if (len(row[2]) > 0) & (row[4] != "\\N"):                   # ignore empty rows.
                if row[2].lower() in IATA_airport_code:                         # check if the city name exists more than once.
                    IATA_airport_code[row[2].lower()].append(row[4].lower())            # map the city - iata airport code and country.
                    IATA_airport_code[row[2].lower()].append(row[3].lower())            # map the city - iata airport code and country.
                else:
                    IATA_airport_code[row[2].lower()] =  [row[4].lower(), row[3].lower()]       # map the city - iata airport code and country.

        return IATA_airport_code                                        # return cleaned up dictionary.


### CACHE DICTIONARY ###
def cache_airport(cache_dict):
    '''
    This function saves the current state
    of the cache to disk.

    :parameter
    -----------

    :returns
    -----------

    '''
    dumped_json_cache = json.dumps(cache_dict, indent=2)               # convert dictionary to json object.
    file = open(CACHE_FILENAME, 'w')                                   # create json file.
    file.write(dumped_json_cache)                                      # write into file.
    file.close()                                                       # close file.


### RETRIEVAL FUNCTION ###
def iata_retrieve(city_name):
    '''
    This function retrieves the IATA code
    based on the city name given.

    :parameter
    -----------

    :returns
    -----------

    '''
    city_name = city_name.lower()
    json_file = open(CACHE_FILENAME, 'r')
    py_file = json.load(json_file)

    IATA_CODE = py_file[city_name]                                                # O(1) search on airport
    if len(IATA_CODE) > 1:                                                        # check if multiple cities.
        print(IATA_CODE)                                                          # display airport codes.
        response = input('Which airport did you mean? Please Input an integer.')  # user prompt.
        result = int(response) - 1
        IATA_CODE = (IATA_CODE[result])                                           # Research the airport code.
        return IATA_CODE                                                          # return iata code.

    return IATA_CODE                                                              # return iata code.


if __name__ == '__main__':
    ### 5602 AIRPORTS ###
    CACHE_DICT = build_airport_dictionary()
    cache_airport(CACHE_DICT)
    print('This dictionary contains ' + str(len(IATA_airport_code)) + ' airports.')

    IATA_CODE = iata_retrieve('DETROIT')
    print(IATA_CODE)