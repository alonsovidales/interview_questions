"""
Print combinations of strings from List of List of String 

Example input: [[quick, slow], [brown, red], [fox, dog]] 

Output: 
    quick brown fox 
    quick brown dog 
    quick red fox 
    quick red dog 
    slow brown fox 
    slow brown dog 
    slow red fox 
    slow red dog

"""

class Combinations(object):
    def __init__(self, words_sets):
        self._words_sets = words_sets

    def combinations(self, pos=None, combs=None):
        if pos is None:
            combs = set()
            pos = [0]*len(self._words_sets)

        combs.add(' '.join([self._words_sets[i][pos[i]] for i in xrange(len(pos))]))

        for i in xrange(len(pos)):
            aux_pos = pos[:]
            aux_pos[i] += 1
            if aux_pos[i] < len(self._words_sets[i]):
                self.combinations(aux_pos, combs)

        return combs

import unittest

class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        cb = Combinations((
            ('quick', 'slow'),
            ('brown', 'red'),
            ('fox', 'dog'),
        ))
        self.assertEqual(
            sorted(cb.combinations()),
            sorted([
                'quick brown fox',
                'quick brown dog', 
                'quick red fox',
                'quick red dog',
                'slow brown fox',
                'slow brown dog',
                'slow red fox',
                'slow red dog'
            ])
        )

if __name__ == '__main__':
    unittest.main()
