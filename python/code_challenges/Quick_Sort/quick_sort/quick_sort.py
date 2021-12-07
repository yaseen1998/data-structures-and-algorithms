def QuicSort(arr):
    length = len(arr)
    if length <=1:
        return arr
    pivot = arr[-1]
    greate =[]
    lower = []
    for item in arr:
        if item > pivot:
            greate.append(item)
        else :
            lower.append(item)
    return QuicSort(lower[:-1]) + [pivot]+QuicSort(greate)







