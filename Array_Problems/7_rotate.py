
#7)Rotate Array by k Positions: Rotate Array to the right by k positions
arr = [1,2,3,4,5]
k = 2
n = len(arr)

k = k % n

arr.reverse()

arr[:k] = reversed(arr[:k])

arr[k:] = reversed(arr[k:])

print(arr) 