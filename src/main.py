# IMPORTS
import wikipedia
import os
import re
import logging
import string
import create_collections
import json
import pickle
import index_collections
from normalize import normalize
from tokenize import tokenize
from sort import alphabetize
import sys
from count import record_occurances
from config import directories as files
from config import indexes as index

if __name__ == '__main__':
    create_collections.create_raw_files()
    index_collections.create_indexes()
    """ __________________________________ """

    
    # Deprecated ---
    # json = json.dumps(counted_documents)
    # f = open(files["index"]+"dict.json","w")
    # f.write(json)
    # f.close()

    #index_collections.create_indexes()
    #create_collections()
    #create_indices()