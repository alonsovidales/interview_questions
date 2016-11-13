"""
. In an unsorted array of numbers that occurs an odd number of times except one that occurs an even number of times, find the number that occurs an even number of times
"""


class ArrInts(object):
	def __init__(self, arr):
		self._arr = arr


	def find_even(self):
		elems = set()
		for e in self._arr:
			if e in elems:
				return e
			elems.add(e)


		return False


import unittest


class TestArrInts(object):
	def test_find_even(self):
		ai = ArrInts((4, 5, 6, 7, 2, 4, ))
		self.assertEquals(ar.find_even(), 4)


		ai = ArrInts(())
		self.assertFalse(ar.find_even())


		ai = ArrInts((1, ))
		self.assertFalse(ar.find_even())


if __name__ == '__main__':
	unittest.main()
