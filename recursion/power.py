def power(base, exponent):
    # base case
    if exponent < 1:
        return 1
    # recursive call
    return base * power(base, exponent-1)

print(power(2,1))