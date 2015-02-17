def square_root(num, precission=0.001):
    x = num
    pow_two = x*x
    while abs(num-pow_two) > precission:
        pow_two = x*x
        x -= (pow_two - num) / (2.0 * x)

    return x

print square_root(4)
print square_root(10)
print square_root(3)
