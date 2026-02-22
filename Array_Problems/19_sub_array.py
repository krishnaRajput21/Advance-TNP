#19)Find Subarray With Given Sum
def subarray_with_sum(arr, target):
    prefix_sum = 0
    seen = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == target:
            return arr[:i+1]

        if (prefix_sum - target) in seen:
            start = seen[prefix_sum - target] + 1
            return arr[start:i+1]

        seen[prefix_sum] = i

    return "No subarray found"
