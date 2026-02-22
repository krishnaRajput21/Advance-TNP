#12)Find the Missing Number

arr = [1,2,4,5,7]
n = len(arr) + 1

s = set(arr)

for num in range(1, n+1):
    if num not in s:
        print("Missing:", num)
