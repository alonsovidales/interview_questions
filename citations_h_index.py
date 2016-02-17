class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		citations = sorted(citations, reverse=True)
		score = 0
		print citations
		for i in xrange(len(citations)):
			print "i:", i, citations[i], score
			if citations[i] > i:
				score = i+1

		return score

																					

print Solution().hIndex([4,4,0,0])
print Solution().hIndex([1,7,9,4])
