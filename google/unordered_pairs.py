"""
Given an array of integer, find the number of un-ordered pairs in that array,
say given {1, 3, 2}, the answer is 1 because {3, 2} is un-ordered, and for
array {3, 2, 1}, the answer is 3 because {3, 2}, {3, 1}, {2, 1}. 
"""

class IntArray(object):
    def __init__(self, int_array):
        self._int_array = int_array
        self._tree = None

    def unordered_pairs_tree(self):
        total = 0
        for v in self._int_array:
            if self._tree is None:
                self._tree = [v, None, None]

            tree = self._tree
            while tree[0] != v:
                if tree[0] > v:
                    total += 1
                    if tree[1] is None:
                        tree[1] = [v, None, None]
                    tree = tree[1]
                else:
                    if tree[2] is None:
                        tree[2] = [v, None, None]
                    tree = tree[2]

        return total

    def unordered_pairs(self):
        total = 0
        for i in xrange(len(self._int_array)):
            for j in xrange(i):
                if self._int_array[j] > self._int_array[i]:
                    total += 1

        return total


import unittest

class TestIntArray(unittest.TestCase):
    def test_unordered_pairs(self):
        ia = IntArray((1, 3, 2,))
        self.assertEqual(ia.unordered_pairs_tree(), ia.unordered_pairs())

        ia = IntArray((3, 2, 1,))
        self.assertEqual(ia.unordered_pairs_tree(), ia.unordered_pairs())

        ia = IntArray(())
        self.assertEqual(ia.unordered_pairs_tree(), ia.unordered_pairs())

if __name__ == '__main__':
    unittest.main()
