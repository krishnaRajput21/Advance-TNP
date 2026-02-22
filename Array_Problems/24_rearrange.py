#24)Rearrange Array Alternately
def rearrange_alternate(arr):
    arr.sort()   # sorting
    
    left = 0
    right = len(arr) - 1
    result = []

    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])
        
        left += 1
        right -= 1

    return result


# Example
arr = [1,2,3,4,5,6]
print(rearrange_alternate(arr))