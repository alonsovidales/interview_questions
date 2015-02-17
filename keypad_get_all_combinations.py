
keypad = [
    [' '],
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z'],
]

def _parse_string(string):
    result = []
    prev_char = string[0]
    current_str = ''
    for c in string:
        if c != prev_char:
            result.append(current_str)
            prev_char = c
            current_str = c
        else:
            current_str += c

    result.append(current_str)

    return result

def _possible_combinations(elems):
    if len(elems) <= 1:
        return 0
    result = 1
    max_sep = len(elems) if len(elems) <= len(keypad[int(elems[0])]) else len(keypad[int(elems[0])])
    for p in xrange(1, max_sep):
        result += _possible_combinations(elems[p:]) + _possible_combinations(elems[:p])

    return result

def map_keys(string):
    parser_str = _parse_string(string)
    print parser_str
    combinations = 1
    for elem in parser_str:
        combinations *= (_possible_combinations(elem) + 1)

    return combinations
    

print _possible_combinations('1111')
print map_keys('1111234112322234144')
