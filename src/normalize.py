from config import directories as files
import os
import string
import sys
import re

def file_to_list( file ):
    with open(file, 'r') as read_file:
        data = read_file.readlines()
    read_file.close()
    return data

def remove_punctuation( data ):
    return [ _.translate( str.maketrans('', '', string.punctuation) ) for _ in data ]

def remove_whitespace( data ):
    return [ __.strip( '\n' ).strip( '\t' ) for __ in data ]

def remove_numbers( data ):
    return [ _.translate( str.maketrans('', '', string.digits) ) for _ in data ]

def remove_case( data ):
    return [ _.lower() for _ in data ]

def normalize( file ):
    file_list = file_to_list(file)
    return remove_case(remove_punctuation(remove_numbers(remove_whitespace(file_list))))
