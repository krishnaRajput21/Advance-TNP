
#18)Move Zeroes to End

def move_zeroes(arr):
    k = 0   # non-zero elements ka index

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[k] = arr[i]
            k += 1

    # remaining positions me 0 bhar do
    while k < len(arr):
        arr[k] = 0
        k += 1

    return arr

# Example
arr = [0,1,0,3,12]
print(move_zeroes(arr))