"""
Given two integer arrays list1 and list2 and an int target value. WAP to check
if there exists such a sum, where one number taken from list1 and other from
list2 to add up to become the target value. Return true if so, else return
false.
"""

def elems_sum_n(list1, list2, n):
    set1 = set(list1)
    for elem in list2:
        if n-elem in set1:
            return True

    return False

import unittest

class TestSumListElems(unittest.TestCase):
    def test_elems_sum_n(self):
        self.assertTrue(elems_sum_n(
            (1, 3, 4, 4,),
            (1, 2, 7, 22, 3, 1,),
            7
        ))

        self.assertFalse(elems_sum_n(
            (1, 1, 1, 1,),
            (1, 1, 1, 1,),
            7
        ))

        self.assertFalse(elems_sum_n(
            (),
            (1, 1, 1, 1,),
            7
        ))

        self.assertFalse(elems_sum_n(
            (1, 1, 1, 1,),
            (),
            7
        ))

        self.assertFalse(elems_sum_n(
            (),
            (),
            7
        ))

if __name__ == '__main__':
    unittest.main()
