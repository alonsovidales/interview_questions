"""
Given a number M (N-digit integer) and K-swap operations(a swap 
operation can swap 2 digits), devise an algorithm to get the maximum possible integer? 
Examples: 
    M = 132 K = 1 output = 312 
    M = 132 K = 2 output = 321 
    M = 7899 k = 2 output = 9987 
    M = 8799 and K = 2 output = 9987
"""

class IntHandler(object):
    def swap(self, num, swaps, max_num=None):
        if max_num is None:
            max_num = [0]

        if swaps == 0:
            if max_num[0] == 0:
                return num
            return max_num[0]

        num_list = list(str(num))
        for i in xrange(len(num_list)):
            for j in xrange(len(num_list)):
                aux = num_list[:]
                aux_int = aux[j]
                aux[j] = aux[i]
                aux[i] = aux_int

                int_num = int(''.join(aux))
                if max_num[0] < int_num:
                    max_num[0] = int_num
                self.swap(int_num, swaps-1, max_num)

        return max_num[0]

import unittest

class TestIntHandler(unittest.TestCase):
    def test_swap(self):
        ih = IntHandler()
        self.assertEqual(ih.swap(132, 1), 312)
        self.assertEqual(ih.swap(132, 2), 321)
        self.assertEqual(ih.swap(7899, 2), 9987)
        self.assertEqual(ih.swap(8799, 2), 9987)
        self.assertEqual(ih.swap(8799, 0), 8799)
        self.assertEqual(ih.swap(0, 3), 0)

if __name__ == '__main__':
    unittest.main()
