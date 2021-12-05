def InsertionSort(arr):
    for j in range(len(arr)-1):
        for i in range(j,len(arr)-1):
            if arr[j]>arr[i+1]:
                arr[j],arr[i+1] = arr[i+1],arr[j]
    return(arr)



