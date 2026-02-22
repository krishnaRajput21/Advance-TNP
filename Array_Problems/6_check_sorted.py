
#6)check if number is sorted or not
arr = [1, 5, 3, 4]

is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print(is_sorted)

