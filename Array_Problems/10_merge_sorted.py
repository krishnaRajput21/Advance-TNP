#10)Merge Two Sorted Arrays
arr1 = [1,3,5]
arr2 = [2,4,6]

i = 0
j = 0
merged = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

# If some elements reamains in first array 
while i < len(arr1):
    merged.append(arr1[i])
    i += 1
# If some elements reamains in second array 
while j < len(arr2):
    merged.append(arr2[j])
    j += 1
print(merged)

