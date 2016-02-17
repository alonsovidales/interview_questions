import collections

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [1]
        i = 2
        while squares[len(squares)-1] < n:
            squares.append(i*i)
            i += 1
            
        print squares
        result = 0
        results = collections.defaultdict(int)
        n_val = n
        for square in squares[::-1]:
            if n_val / square > 0:
                results[square] += n_val / square
		result += n_val / square
            n_val %= square
            print square, results, n_val
            
        return result

print Solution().numSquares(13)
