"""
25

Given a list of coin values, and quantity of each type of coin. Write a 
program to return the set of all possible sums which can be made using those 
coins. 
ex. coins = [10, 50, 100, 500] 
quantity = [5, 3, 2, 2] 
sum could be 400 , 300 ,200 , 100 << This can't be correct
"""

class Coins(object):
    def __init__(self, coins):
        self._coins = coins

    def sums(self, quantities, sums=None, known_comb = set()):
        if sums is None:
            sums = set()

        for i in xrange(len(quantities)):
            quantities_aux = quantities[:]
            quantities_aux[i] -= 1
            if tuple(quantities_aux) in known_comb:
                continue

            known_comb.add(tuple(quantities_aux))
            if quantities_aux[i] >= 0:
                sums.add(sum([x[0]*x[1] for x in zip(self._coins, quantities)]))
                sums &= self.sums(quantities_aux, sums, known_comb)

        return sums

import unittest

class TestCoins(unittest.TestCase):
    def test_sums(self):
        cin = Coins((10, 50, 100, 500,))
        # I think that the example is not correct
        self.assertEqual(
            set(cin.sums([5, 3, 2, 2])),
            set((400 , 300 ,200 , 100,))
        )

if __name__ == '__main__':
    unittest.main()
