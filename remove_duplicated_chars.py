class Solution(object):
	def _isPossible(self, s, sub_str):
		return True

	def removeDuplicateLetters(self, s, result=None, min_result=None):
		"""
		:type s: str
		:rtype: str
		"""
		print set(list(s))

print Solution().removeDuplicateLetters("bcabc")
print Solution().removeDuplicateLetters("cbacdcbc")
