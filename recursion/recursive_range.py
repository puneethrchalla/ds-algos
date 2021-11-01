def recursive_range(num):
    if num == 1:
        return 1
    return num + recursive_range(num-1)

print(recursive_range(6)) # 21
print(recursive_range(10)) # 55