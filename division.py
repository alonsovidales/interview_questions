# a/b
def add(x, y):
    a = True
    while a:
        a = x & y
        b = x ^ y
        x = a << 1
        y = b

    return b

def mult(a, b):
    r = 0
    for i in xrange(b):
        r = add(r, a)

    return r

def division(a, b, precission=0.001):
    prev_guess = 0
    guess = a
    while abs(a - mult(guess, b)) > precission:
        aux = guess
        if mult(guess, b) > a:
            guess -= abs(guess - prev_guess) / 2
        else:
            guess += abs(guess - prev_guess) / 2

        prev_guess = aux

    return guess

print division(10, 2)
print division(12, 3)
