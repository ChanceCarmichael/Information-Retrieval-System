from config import indexes
NGRAMS = []
def test():
    """ Gets user input for what's supposed to be in the document collection """
    return input("test")

def check_spelling( term ):
    check_bigrams = split_into_bigrams( term )
    return check_bigrams

def split_into_bigrams( word ):
    word_list = [char for char in word]
    ret_list = []
    place = 0
    for letter in word_list:
        
        if place == 0:
            place = place + 1
            continue

        if word_list[place] == " ":
            break
        ret_list.append(word_list[place-1] + word_list[place])
        place = place + 1
    return ret_list

def check_against_index( word,test, sim ):
    with open ( indexes['ngram-term'], 'r' ) as read_file:
        for line in read_file:
            ngrams,term = line.split(" => ")
            NGRAMS.append( (list(filter(bool,ngrams.split('.'))),term.strip()) )
    read_file.close()
    matches = []
    for nlist,term in NGRAMS:
        if test == "jacquard":
            if test_jacquard_similarity(word,nlist) > sim:
                matches.append(term)
    return matches

def test_jacquard_similarity( list_1, list_2 ):
    inter = len(set(list_1).intersection(set(list_2)) )
    un = len(set(list_1).union(set(list_2)) )
    return ( inter / un )

def spellcheck(term, test="jacquard", gran=0.5):
    
    ngrams = split_into_bigrams( term )
    match_list = check_against_index( ngrams, test, gran )
    