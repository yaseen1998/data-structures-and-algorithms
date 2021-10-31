def reverseArray (arr):
    result=[]
    for i in range(len(arr)-1, -1, -1):
        result.append(arr[i]),
    return result

print(reverseArray([1,2,3,4,5]))
