def Mergesort(arr):
    n= len(arr)
    if n>1:
        mid =int(n/2)
        left=arr[:mid]
        right = arr[mid:]
        Mergesort(left)
        Mergesort(right)
        Merge(left, right, arr)
        return(arr)
## visual
this function use to split the array until one number
arr = [1,2,3]
left = [1]
right = [2,3] => left = [2] , right=[3] ,arr =[2,3]

def Merge(left, right, arr):
    i,j,k=0,0,0
    while i < len(left) and j < len(right):
        if left[i]<= right[j]:
            arr[k]=left[i]
            i=i+1
        else:
            arr[k]=right[j]
            j=j+1
        k=k+1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

left = [2] , right=[3] ,arr =[2,3]
check if left smaller or equal than right change a first element in arr to first element in left
else change a first element in arr to first element in right
