#16)Check if Two Arrays Are Equal
from collections import Counter

def are_arrays_equal(arr1, arr2):
    return Counter(arr1) == Counter(arr2)

arr1 = [1,2,2,3]
arr2 = [2,5,1,2]

print(are_arrays_equal(arr1, arr2))