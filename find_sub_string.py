def search(haystack, needle):
    w = 0
    fw = 0
    for c in needle:
        fw += ord(c)

    fw %= 997
    for i in range(0, len(needle)):
        w += ord(haystack[i])

    if fw == w % 997:
        if needle == haystack[:len(needle)]:
            return 0

    for i in range(len(needle), len(haystack)):
        w += ord(haystack[i])
        w -= ord(haystack[i-len(needle)])
        if w % 997 == fw:
            print needle, haystack[i-len(needle)+1:i+1]
            if needle == haystack[i-len(needle)+1:i+1]:
                return i-len(needle)+1
    
    return False

haystack = "this is a test string in order to proof one thing"
needle = "proof"

print haystack.find(needle)
print search(haystack, needle)
