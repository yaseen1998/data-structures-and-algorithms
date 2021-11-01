def insertShiftArray(arr,insert):

    length = ceil(len(arr)/2)
    result= arr+[insert]
    result[length],result[len(result)-1]=result[len(result)-1],result[length]
    return result

def ceil(num):
    floor = int(num)
    if floor != num:
        return floor + 1
    return floor

print(insertShiftArray([1,2,3,4,5],7))
