"""
You have a sorted array of integers. Find the element where the array index is
equal to the value of the corresponding element. Or return that no such element
exists.

(I assume that we can't have duplicated integers...)
"""

def get_equal_index_value(ints, l=0, r=None):
	# Using binary search to solve the problem
	if r is None:
		r = len(ints)-1

	if r-l <= 1:
		return None

	center = (r-l)/2+l

	if ints[center] == center:
		return center
	if ints[center] > center:
		return get_equal_index_value(ints, l, center)

	return get_equal_index_value(ints, center, r)


print get_equal_index_value([-1, 0, 1, 2, 3, 4, 6, 8])
