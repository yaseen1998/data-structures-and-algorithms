def BinarySearch (arr, n):
    start = 0
    end = len(arr) - 1
    mid = 0

    while start <= end:
        mid = (end + start) // 2
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            return mid
    return -1

arr = [12, 24, 32, 39, 45, 50, 54]
n = 45

# Function call
result = BinarySearch (arr, n)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not exist")
