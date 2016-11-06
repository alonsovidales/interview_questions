"""
Find the minimum of every sub-array of size k in an array of size n. 

O(n) solution required.

Note: I really thik that is not possible to resolve this in O(n), all the
provided solutions from: https://www.careercup.com/question?id=5717731845341184
has O(kn) or are not correct
"""

def sub_array_min_search(elems, sub_len):
    if len(elems) == 0 or sub_len == 0:
        return []

    return [min(elems[i:i+sub_len]) for i in xrange(len(elems)-sub_len+1)]

import unittest

class TestArraySearch(unittest.TestCase):
    def test_sub_array_min_search(self):
        self.assertEquals(
                sub_array_min_search([1, 2, 3, 4, 5], 2),
                [1, 2, 3, 4])

        self.assertEquals(
                sub_array_min_search([123, 4, 5, 6, 1], 2),
                [4, 4, 5, 1])

        self.assertEquals(
                sub_array_min_search([], 2),
                [])

        self.assertEquals(
                sub_array_min_search([1], 2),
                [])

        self.assertEquals(
                sub_array_min_search([123, 4, 5, 6, 1], 0),
                [])

if __name__ == '__main__':
    unittest.main()
