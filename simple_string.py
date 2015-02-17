def string_processor(string):
    result = ''
    for c in string:
        if c == 'a':
            result += 'aa'
        elif c != 'b':
            result += c

    return result

string = 'aajfjknwqdnqlwbbalknbaba'
print string
print string_processor(string)
