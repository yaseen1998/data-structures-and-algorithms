import re 
def hash(text):
    strr = re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower()))
    dic = set()
    for char in strr:
        if char in dic:
            return char
        else:
            dic.add(char)
    return 'no element repeat'
