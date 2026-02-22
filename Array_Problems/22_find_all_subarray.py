#22)Find All Subarrays
def find_all_subarrays(arr):
    n = len(arr)

    for start in range(n):
        for end in range(start, n):
            print(arr[start:end+1])


# Example
arr = [1,2,3]
find_all_subarrays(arr)
