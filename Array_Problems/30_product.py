#30Product of Array Except Self

def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    # Step 1: Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]

    # Step 2: Right products
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= arr[i]

    return result

# Example
arr = [1,2,3,4]
print(product_except_self(arr))
