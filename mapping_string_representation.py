def numreps(s):
    length = len(s)
    if length == 0:
        return 1
    if length >= 2 and 10 < int(s[:2]) <= 26:
        return numreps(s[1:]) + numreps(s[2:])

    return numreps(s[1:])

print numreps('123122123')
