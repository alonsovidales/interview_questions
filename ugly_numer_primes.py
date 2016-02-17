class Solution(object):
    def __init__(self):
        self._factors = set([1, 2, 3, 5])

    def _sieveOfEratosthenes(self, n):
        # Using the Sieve of Eratosthenes calculate
        # all the primes and ugly numbers to n
        i = 0
        nums = set([])
        while len(nums) < n:
            nums |= set(range(n*i+1, n*(i+1)+1))
	    to_discard = set([])
            for num in xrange(2, n*(i+1)+1):
                for a in xrange(2, n*(i+1)+1):
                    if a in self._factors and num in self._factors:
                        continue
                    to_discard.add(a*num)
                    print a, num, a*num

            nums -= to_discard
            # Remove all the primes
            to_discard = set([])
	    for num in nums:
	        disc = True
	        for fact in self._factors:
                    if fact != 1 and num % fact == 0:
                        disc = False
		if disc:
                    to_discard.add(num)
            nums -= to_discard

            i += 1
        
	nums.add(1)
        return sorted(nums)
        
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
	ugly_nums = self._sieveOfEratosthenes(n)
	print ugly_nums
        return ugly_nums[n-1]

print Solution().nthUglyNumber(11)
