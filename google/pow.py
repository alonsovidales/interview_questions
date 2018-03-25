def power_of(a, b, cache=None):
    if cache is None:
        cache = {}

    if b not in cache:
        print "MISS", b, cache
        if b == 0:
            cache[b] = 1
        elif b == 1:
            cache[b] = a
        else:
            int_pow = power_of(a, b//2, cache)

            cache[b] = int_pow * int_pow
            if b%2 == 1:
                cache[b] *= a
    else:
        print "HIT", b
    
    return cache[b]

print power_of(10, 100)
