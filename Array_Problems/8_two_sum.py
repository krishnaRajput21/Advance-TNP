#8)Find pair with given sum
arr = [2, 4, 11, 17]
target = 15

seen = {}

for i in range(len(arr)):
    complement = target - arr[i]
    
    if complement in seen:
        print("Pair Found:", complement, arr[i])
        break
    
    seen[arr[i]] = i
