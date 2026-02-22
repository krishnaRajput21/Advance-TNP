#13)Find Duplicates in Array
arr = [1,2,3,1,3,6,6]
seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(list(duplicates))