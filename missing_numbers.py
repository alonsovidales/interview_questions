class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected = 0
        obtained = 0
        for i in xrange(len(nums)):
            expected ^= i
            obtained ^= nums[i]
            
        expected ^= len(nums)
        
        return expected ^ obtained
