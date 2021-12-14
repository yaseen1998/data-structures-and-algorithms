from hashtable import HashTable

def left_join(hash1,has2):
    result = []
    for key,value in (hash1.items()):
        value2 = None
        if has2[key]:
            value2 = has2[key]
        result.append([key,value,value2])
    return result

def right_join(hash1,has2):
    result = []
    for key,value in (has2.items()):
        value2 = None
        if hash1[key]:
            value2 = hash1[key]
        result.append([key,value,value2])
    return result