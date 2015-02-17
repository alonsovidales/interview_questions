from collections import deque

_operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

__high_prio_ops = set(['/', '*'])

def _parse_string(string):
    result = deque()

    current_num = ''
    for c in string:
        if c in _operators:
            result.append(float(current_num))
            result.append(c)
            current_num = ''
        else:
            current_num += c

    result.append(float(current_num))

    return result

def calculate(string):
    elems = _parse_string(string)
    num_stack = [elems.popleft()]
    op_stack = []

    while len(elems) > 0:
        op = elems.popleft()
        if op in __high_prio_ops:
            num_right = elems.popleft()
            num_left = num_stack.pop()
            num_stack.append(_operators[op](num_left, num_right))
        else:
            op_stack.append(op)
            num_stack.append(elems.popleft())

    while len(op_stack) > 0:
        num_right = num_stack.pop()
        num_left = num_stack.pop()
        op = op_stack.pop()
        num_stack.append(_operators[op](num_left, num_right))

    return num_stack[0]

print calculate("2+4*5*7")
print calculate("2+4*5+1.3")
print calculate("2+4+5.6-7")
print calculate("2")
print calculate("2/2")
