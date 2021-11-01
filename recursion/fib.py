def fib(num):
    # base case
    if num == 1 or num == 2:
        return 1
    # call recursively
    return fib(num-1) + fib(num-2)

print(fib(5)) # 3
print(fib(10)) # 55
print(fib(28)) # 317811