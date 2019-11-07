import wikipedia
import os
import re
import logging
import string

USER_MESSAGES = [
    "Which articles would you like to get content from? Please enter a comma separated list for the sake of this project please.\n",
    "Disambiguation, couldn't retrieve article for the search term: ",
]

def get_user_content_query():
    """ Gets user input for what's supposed to be in the document collection """
    return input(USER_MESSAGES[0])

def sanitize(query):
    query = query.replace(', ', ',')
    return query.split(',')

def get_wikipedia_content(query):
    search_terms = sanitize(query)
    for term in search_terms:
        temp_content = ""
        try:
            temp_content = wikipedia.page(term).content
            filename = os.path.join("raw_text", term + ".raw")
            write_file = open(filename, 'x')
            write_file.write(temp_content)
            write_file.close()
        except wikipedia.exceptions.DisambiguationError:
            print (USER_MESSAGES[1] + term)

def create_raw_files():
    user_wikipedia_query = get_user_content_query()
    get_wikipedia_content(user_wikipedia_query)