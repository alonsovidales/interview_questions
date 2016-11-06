"""
Given a sparse matrix, implement below two methods: 
    void set(int row, int col, int val) /*Update value at given row and col*/ 

    int sum(int row, int col) /*give sum from top left corner to given row, col sub-matrix*/
"""
class SortedArray(object):
    def __init__(self):
        self._dirty = False
        self._arr = []
        self._elems = {}

    def set(self, val, score):
        self._elems[score] = val
        self._arr.append((val, score))
        self._dirty = True

    def get_by_score(self, score):
        return self._elems.get(score)

    def get_to_score(self, score):
        if self._dirty:
            self._arr = sorted(self._arr, key=lambda x: x[1])
            self._dirty = False

        result = []
        for i in xrange(len(self._arr)):
            if self._arr[i][1] > score:
                return result

            result.append(self._arr[i][0])

        return result

class SparseMatrix(object):
    def __init__(self):
        self._rows = SortedArray()

    def set(self, row, col, v):
        cols = self._rows.get_by_score(row)
        if cols is None:
            cols = SortedArray()
            self._rows.set(cols, row)

        cols.set(v, col)

    def sum(self, row, col):
        total = 0
        for cols in self._rows.get_to_score(row):
            for value in cols.get_to_score(col):
                total += value

        return total

import unittest

class TestSparseMatrix(unittest.TestCase):
    def test_set_sum(self):
        sm = SparseMatrix()
        sm.set(1, 2, 1)
        sm.set(3, 2, 2)
        sm.set(9, 1, 3)
        sm.set(3, 8, 4)

        self.assertEqual(sm.sum(1, 2), 1)
        self.assertEqual(sm.sum(9, 9), 10)
        self.assertEqual(sm.sum(3, 2), 3)

if __name__ == '__main__':
    unittest.main()
