
#11)Remove Given Element from Array
arr = [3,2,2,3,5,7,6,8]
val = 3

result = []

for num in arr:
    if num != val:
        result.append(num)

print(result)
