def product_array(arr):
    # base case
    if len(arr) < 1:
        return -1
    if len(arr) == 1:
        return arr[0]
    return arr[0] * product_array(arr[1:])

print(product_array([9,9]))