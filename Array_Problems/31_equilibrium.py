#31)Find Equilibrium Index

def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


# Example
arr = [1,3,5,2,2]
print(equilibrium_index(arr))