
def binary_search(s_arr, start, end, num):
    # base case
    if start > end:
        return -1
    # calling func recursively
    middle = (start + end) // 2
    if s_arr[middle] == num:
        return middle
    elif s_arr[middle] < num:
        return binary_search(s_arr, middle+1, end, num)
    else:
        return binary_search(s_arr, start, middle-1, num)

array = [1,3,5,7,9]
result = binary_search(array, 0, 4, 7)
print(result)

