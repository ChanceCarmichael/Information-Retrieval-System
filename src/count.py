def record_occurances( data ):
    tmp_list = []
    for item in data:
        tmp_list.append((item, data.count(item)))
    return sorted(list(set(tmp_list)))