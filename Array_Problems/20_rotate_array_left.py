#20)Rotate Array to Left by k Positions

def left_rotate(arr, k):
    n = len(arr)
    k = k % n  
    
    return arr[k:] + arr[:k]


# Example
arr = [1,2,3,4,5]
k = 2
print(left_rotate(arr, k))

