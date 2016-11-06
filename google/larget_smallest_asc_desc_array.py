"""
Find the largest and smallest number in a list. The list is stored as two sections, one in ascending order and the other in descending order. 

input [2 3 4 5 6 7 10 9 8 7] 
smallest : 2 
Largest 10
"""
class AscDesc(object):
    def __init__(self, numbers):
        self._numbers = numbers

    def get_min_max(self):
        if len(self._numbers) == 0:
            return 0, 0

        largest_pos = len(self._numbers)/2
        step = largest_pos/2

        while not self._numbers[largest_pos-1] < self._numbers[largest_pos] > self._numbers[largest_pos+1] and step != 0:
            if self._numbers[largest_pos-1] > self._numbers[largest_pos]:
                largest_pos -= step
                step /= 2
            else:
                largest_pos += step
                step /= 2

        smallest = min(self._numbers[0], self._numbers[-1])
        if  not self._numbers[largest_pos-1] < self._numbers[largest_pos] > self._numbers[largest_pos+1]:
            return smallest, max(self._numbers[0], self._numbers[-1])

        return smallest, self._numbers[largest_pos]

import unittest

class TestAscDesc(unittest.TestCase):
    def test_get_min_max(self):
        asc_desc = AscDesc((2, 3, 4, 5, 6, 7, 10, 9, 8, 7))
        self.assertEqual(asc_desc.get_min_max(), (2, 10))

        asc_desc = AscDesc(())
        self.assertEqual(asc_desc.get_min_max(), (0, 0))

        asc_desc = AscDesc((1, 2, 3))
        self.assertEqual(asc_desc.get_min_max(), (1, 3))

        asc_desc = AscDesc((1, ))
        self.assertEqual(asc_desc.get_min_max(), (1, 1))

        asc_desc = AscDesc((3, 2, 1))
        self.assertEqual(asc_desc.get_min_max(), (1, 3))

        asc_desc = AscDesc((2, 3, 2, 1))
        self.assertEqual(asc_desc.get_min_max(), (1, 3))

if __name__ == '__main__':
    unittest.main()
