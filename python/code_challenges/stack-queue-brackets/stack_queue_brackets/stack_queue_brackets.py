def prack(string):
    prack1 = ['[','{','(']
    prack2 = [']','}',')']
    stack =[]
    for char in string:
        if char in prack1:
            stack.append(char)
        elif char in prack2:
            current_char = stack.pop()
            ind = prack1.index(current_char)
            if char !=prack2[ind]:
                return False

    return True
