"""
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.* 


Example:




Input:  arr[] = {1, 2, 3, -4, -1, 4}
    Output: arr[] = {-4, 1, -1, 2, 3, 4}
    
    Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
    output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}

"""

class ArrInts(object):
	def __init__(self, arr):
		self._arr = arr


	def neg_pos(self):
		neg_nums = [x for x in self._arr if x < 0]
		pos_nums = [x for x in self._arr if x >= 0]


		result = []
		p = 0
		n = 0
		add_pos = False
		for i in xrange(len(self._arr)):
			if (add_pos and p < len(pos_nums)) or n >= len(neg_nums):
				result.append(pos_nums[p])
				p += 1
			else:
				result.append(neg_nums[n])
				n += 1


			add_pos = not add_pos


		return tuple(result)


import unittest


class TestArrInts(unittest.TestCase):
	def test_neg_pos(self):
		ai = ArrInts((1, 2, 3, -4, -1, 4,))
		self.assertEqual(ai.neg_pos(), (-4, 1, -1, 2, 3, 4,))


		ai = ArrInts((-5, -2, 5, 2, 4, 7, 1, 8, 0, -8,))
		self.assertEqual(ai.neg_pos(), (-5, 5, -2, 2, -8, 4, 7, 1, 8, 0,))


		ai = ArrInts((-1,))
		self.assertEqual(ai.neg_pos(), (-1,))


		ai = ArrInts((1,))
		self.assertEqual(ai.neg_pos(), (1,))


		ai = ArrInts(())
		self.assertEqual(ai.neg_pos(), ())




if __name__ == '__main__':
	unittest.main()
