#33)Find Maximum Difference
def max_difference(arr):
    min_value = arr[0]
    max_diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        max_diff = max(max_diff, arr[i] - min_value)
        min_value = min(min_value, arr[i])

    return max_diff


# Example
arr = [2,3,10,6,4,8,1]
print(max_difference(arr))
