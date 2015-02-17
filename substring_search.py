# Rabin-Karp algorithm
# Another option is the KMP algorithm: http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

def strstr(needle, haystack):
    weight = 0
    for c in needle:
        weight += ord(c)
        weight %= 997

    curr_weight = 0
    for i in xrange(len(needle)):
        curr_weight += ord(haystack[i])

    if needle == haystack[:len(needle)]:
        return haystack

    for i in xrange(len(needle), len(haystack)):
        curr_weight += ord(haystack[i])
        curr_weight -= ord(haystack[i-len(needle)])
        curr_weight %= 997
        if curr_weight == weight and needle == haystack[i-len(needle)+1:i+1]:
            return haystack[i-len(needle)+1:]

    return False

print strstr("this", "checking this function in order to know how it works...")
print strstr("it", "checking this function in order to know how it works...")
print strstr("in", "checking this function in order to know how it works...")
print strstr("aaaaaa", "checking this function in order to know how it works...")
