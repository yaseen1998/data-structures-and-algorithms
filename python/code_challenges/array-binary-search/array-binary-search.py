def BinarySearch (arr, n):
    start = 0
    end = len(arr) - 1
    mid = 0

    while start <= end:
        # for get integer result
        mid = (end + start) // 2

        # Check if n is present at mid
        if arr[mid] < n:
            start = mid + 1

        # If n is greater, compare to the right of mid
        elif arr[mid] > n:
            end = mid - 1

        # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return -1

arr = [12, 24, 32, 39, 45, 50, 54]
n = 45

# Function call
result = BinarySearch (arr, n)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not exist")
