import os
import re
import logging
import string
from normalize import normalize
from tokenize import tokenize
from sort import alphabetize
from count import record_occurances
from config import directories as files
from config import indexes as index
import sys

def create_heading_index( sorted_documents ):
    with open(index['header-document'], 'w') as write_file:
        for key,value in sorted_documents.items():
            for term in value:
                print(term)
                if re.match('={1,3}\ .*?\ ={1,3}', term):
                    write_file.write(term.strip('==') + '\n')
    write_file.close()

def create_ngram_term_index( n_size=2 ):
    
    with open( index['term-document'], 'r' ) as read_file:
        with open( index['ngram-term'], 'w' ) as write_file:
            write_file.seek(1)
            for term in read_file:
                item,_ = term.split(" {")
                # write_file.write(term)
                ble = [char for char in item]
                list = []
                place = 0
                for character in ble:

                    if place == 0:
                        place = place + 1
                        continue

                    if ble[place] == " ":
                        break
                    list.append(ble[place-1] + ble[place])
                    place = place + 1

                return_string = ""
                for hyd in list:
                    return_string = return_string + hyd +"."
                write_file.write(return_string + " => " + item +"\n")

        write_file.close()
    read_file.close()

def create_term_document_index( sorted_documents ):
    document_occurances = {}
    for document, occurences in sorted_documents.items():
        for term in occurences:
            if term not in document_occurances:
                document_occurances[term] = [document]
            else:
                document_occurances[term].append(document)

    with open (index["term-document"], "a") as write_file:
        for key, value in document_occurances.items():
            write_file.write(key + " " + str(set(value)) + '\n')
    write_file.close()

def create_term_document_occurence_index( sorted_documents ):
    with open (index["term-occurence-document"], "w") as write_file:
        for key, value in sorted_documents.items():
            ble = record_occurances(value)
            for term, occurence in ble:
                write_file.write(str(key)+"."+term+"."+str(occurence) + "\n")
    write_file.close()
    
def create_indexes():
    documents ={}
    doc_id = 0

    # For each document in the raw_text directory...
    # 1 - Normalize the information
    # 2 - Tokenize the information
    # 3 - Assign it a document id as a key and a list of tokens as the value
    for raw_file in os.listdir( files["raw_text"] ):
        
        filepath = files["raw_text"] + raw_file
        normalized = normalize( filepath )
        tokens = tokenize( normalized )
        documents[doc_id] = tokens
        doc_id = doc_id + 1
    
    
    # For each docment in the document dictionary (in memory)...
    # We'll alphabetize the  value (a list of tokens)
    sorted_documents = {}
    for key, value in documents.items():
        sorted_documents[key] = alphabetize(value)
    
    create_term_document_index( sorted_documents )
    create_term_document_occurence_index( sorted_documents )
    create_ngram_term_index()
    