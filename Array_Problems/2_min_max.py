#2)Find the Maximum & Minimum Element
arr = [5,3,2,9]
maximumm = arr[0]
minimum = arr[0]
for num in arr:
    if num > maximumm:
        maximumm = num
    if num < minimum:
        minimum = num
print("Maximum:", maximumm)
print("minimum:", minimum)            
