#32)Find Maximum Product Pair

def max_product_pair(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        # Find two largest
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        # Find two smallest
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # Compare products
    if max1 * max2 > min1 * min2:
        return (max1, max2)
    else:
        return (min1, min2)


# Example
arr = [-10, -3, 5, 6, -2]
print(max_product_pair(arr))