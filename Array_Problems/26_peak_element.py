#26)Find Peak Element
def find_peak(arr):
    n = len(arr)

    for i in range(n):
        if (i == 0 or arr[i] > arr[i-1]) and \
           (i == n-1 or arr[i] > arr[i+1]):
            return arr[i]


arr = [1,2,3,1]
print(find_peak(arr))