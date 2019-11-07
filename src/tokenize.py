
def listify( list ):
    tmp = filter(lambda item: item != '', list)
    return_list = []
    for item in tmp:
        _ = item.split(' ')
        return_list.append(_)
    return return_list

def tokenize( data ):
    list = listify( data )
    flatten = lambda _ : [ item for sublist in _ for item in sublist ]
    return flatten( list )