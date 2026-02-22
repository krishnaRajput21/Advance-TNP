#9)remove duplicate from array
arr = [1,2,3,1,5,2,3,1,4]

seen = set()
result = []

for num in arr:
    if num not in seen:
        result.append(num)
        seen.add(num)
print(result)