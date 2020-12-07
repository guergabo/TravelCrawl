# File: data_sources.py
# Description: This file provides the database schema and functionality.
# Name: Gabriel Guerra
# Uniqname: Guergabo
# Date-Modified: 12-06-2020

### PACKAGES ###
import data_sources as ds           # importing functions from data_sources.py,
import sqlite3                      # python package for sqlite relational databases.

'''
API DESIGN NOTES:
+ ------------------------ +
| Request Path Parameters  |
+ ------------------------ +
1. dep_loc: the origin place.
2. des_loc: the destination place.
3. dep_date: the outbound date.
4. ret_date: the return date.
+ ------------------------ +
| Response Parameters      |
+ ------------------------ +
1. Quotes: contains the list of cheapest quotes available for the search.
2. Places: the list of places matching the search results.
3. Carriers: the list of carriers specified in the list of quotes.
4. Currencies: the currency of the quote prices.
'''

### CREATE DATABASE ###
def db_create():
    '''
    This function create a database schema
    using the data from data_source.py.

    :parameter
    -----------

    :returns
    -----------

    '''
    pass

### READ DATABASE ###
def db_read():
    '''
    This function allows the user to retrieve
    any data from the database.

    :parameter
    -----------

    :returns
    -----------

    '''
    pass

### UPDATE DATABASE ###
def db_update():
    '''
    This function allows the user to update the
    database.

    :parameter
    -----------

    :returns
    -----------

    '''
    pass

### DELETE DATABASE ###
def db_delete():
    '''
    This function allows the user to partially ot
    entirely delete the database.

    :parameter
    -----------

    :returns
    -----------

    '''
    pass


### CACHE DATA ###
def db_cache(source):
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
    pass