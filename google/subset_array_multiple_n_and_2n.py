"""
Given an arraylist of N integers, 
(1) find a non-empty subset whose sum is a multiple of N. 
(2) find a non-empty subset whose sum is a multiple of 2N. 
Compare the solutions of the two questions.
"""

class IntArray(object):
    def __init__(self, int_arr):
        self._int_arr = int_arr

    def sum_mult_n(self, n, subset=None):
        if subset is None:
            subset = self._int_arr

        if sum(subset) == n:
            return subset

        for i in xrange(len(subset)):
            aux_subset = subset[:i] + subset[i+1:]
            sum_subset = self.sum_mult_n(n, aux_subset)
            if sum_subset is not None:
                return sum_subset

        return None

import unittest

class TestIntArray(unittest.TestCase):
    def test_sum_mult_n(self):
        ia = IntArray([2, 3, 4, 6])
        self.assertEqual(sum(ia.sum_mult_n(5)), 5)

        ia = IntArray([])
        self.assertEqual(ia.sum_mult_n(5), None)

        ia = IntArray([1, 9])
        self.assertEqual(ia.sum_mult_n(1), [1])

if __name__ == '__main__':
    unittest.main()
