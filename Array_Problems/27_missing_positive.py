#27)Find the First Missing Positive
def first_missing_positive(arr):
    n = len(arr)

    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i]-1] != arr[i]:
            correct_index = arr[i] - 1
            arr[i], arr[correct_index] = arr[correct_index], arr[i]

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1

# Example
arr = [3,4,-1,1]
print(first_missing_positive(arr))
