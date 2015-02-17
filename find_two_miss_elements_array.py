
def find_missing(arr):
	s = [False] * (len(arr)+1)
	for i in arr:
		s[i-1] = True

	nums = []
	for i in xrange(len(s)):
		if not s[i]:
			nums.append(i+1)
			if len(nums) == 2:
				return nums

	return False

print find_missing([1, 3, 4, 4, 5, 6, 7, 8])
print find_missing([1, 2, 4, 5, 6, 8, 8, 9])
