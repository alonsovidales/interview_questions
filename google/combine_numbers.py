# Combine two digits of a number. Return the largest. For example, given 4621,
# return 521.  
# I have no idea how to get a 5 combining 4 and 6, just the mean but that doesn't makes sense.
# I'll use a xor to combine

def get_int(arr_dig):
    result = arr_dig[0]
    for i, v in enumerate(arr_dig[1:]):
        result += v * pow(10, i+1)

    return result

def combine_digits(integer):
    digits = []
    int_aux = integer
    while int_aux > 0:
        digits.append(int_aux % 10)
        int_aux /= 10

    max_comb = float('-inf')
    for y in xrange(len(digits)):
        for x in xrange(len(digits)):
            if y == x:
                continue

            aux_digits = digits[:]
            aux_digits[x] = digits[x] ^ digits[y]
            aux_digits.pop(y)
            value = get_int(aux_digits)
            if value > max_comb:
                max_comb = value

    return max_comb

import unittest

class TestStringMethods(unittest.TestCase):
    def test_smallest_num(self):
        self.assertEqual(combine_digits(4621), 521)

if __name__ == '__main__':
    unittest.main()
