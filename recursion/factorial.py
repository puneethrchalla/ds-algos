def factorial(num):
    # base case
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)

print(factorial(7))