class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        sorted = False
        while not sorted:
            sorted = True
            for i in xrange(len(nums)-1):
                if nums[i] == 0 and nums[i+1] != 0:
                    aux = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = aux
                    sorted = False
