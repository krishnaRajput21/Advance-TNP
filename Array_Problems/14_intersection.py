#14)Find Intersection of Two Arrays
arr1 = [1,2,2,3,1]
arr2 = [2,2,3]

set1 = set(arr1)
set2 = set(arr2)

intersection = list(set1 & set2)

print(intersection)