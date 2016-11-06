"""
Given an Array A with n elements. Pick maximum number of elements from given array following the rule: 
    1. We cannot pick A[i] and A[j] if absolute value of (A[i] - A[j]) > absolute value of (i - j) 

Example: {13,5,4} 
Ans: 2 
Pick 5 and 4.
"""

def get_elems(elems):
    total = 0
    used_pos = set()
    for i in xrange(len(elems)):
        for j in xrange(i+1, len(elems)):
            if abs(elems[i] - elems[j]) <= abs(i-j):
                if i not in used_pos:
                    total += 1
                    used_pos.add(i)
                if j not in used_pos:
                    total += 1
                    used_pos.add(j)

    return total

import unittest

class TestArrFinder(unittest.TestCase):
    def test_get_elems(self):
        self.assertEqual(get_elems((13, 5, 4)), 2)

        self.assertEqual(get_elems((13, 5, 4, 3)), 3)

        self.assertEqual(get_elems((13, 1, 1, 1)), 3)

        self.assertEqual(get_elems(()), 0)

        self.assertEqual(get_elems((1, )), 0)

if __name__ == '__main__':
    unittest.main()
