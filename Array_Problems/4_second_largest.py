
#4)Second Largest Element
arr = [5,21,45,23,33,20]

first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num < first:
        second = num

if second == float('-inf'):
    print("No second largest element")
else:
    print("Second Largest:", second)