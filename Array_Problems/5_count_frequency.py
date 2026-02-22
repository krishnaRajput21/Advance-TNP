#5)Count Frequency of Element
arr = [1,2,2,3,4,4,4,4,5,6,7,8,8,8,8,9]
freq = {}
for num in arr:
    if num in freq:
        freq[num] +=1
    else:
        freq[num] = 1
print(freq)            