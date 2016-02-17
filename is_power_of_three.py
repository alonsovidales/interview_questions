class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Using Binary search from 1 to n in
        # order to find the possible number
        left = 1
        right = n
        while right-left > 1:
            center = (right-left)/2+left
            print right, left, center
            pow_three = center * center * center
            if pow_three == n:
                return True
            if center * center * center > n:
                right = center
            else:
                left = center
            
        return False
