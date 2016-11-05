"""
Given an NxN grid with an array of lamp coordinates. Each lamp provides
illumination to every square on their x axis, every square on their y axis, and
every square that lies in their diagonal (think of a Queen in chess). Given an
array and query coordinates, determine whether that point is illuminated or not.
The catch is when checking a query all lamps adjacent to, or on,
"""

class LampsMatrix(object):
    def __init__(self, lamps):
        self._lamps = lamps

    def is_iluminated(self, x, y):
        for lamp in self._lamps:
            if x == lamp[0] or y == lamp[1] or abs(x-lamp[0]) == abs(y-lamp[1]):
                return True

        return False

import unittest

class TestLampsMatrix(unittest.TestCase):
    def test_is_iluminated(self):
        lm = LampsMatrix((
            (1, 1),
            (10, 4),
            (4, 4),
        ))
        self.assertTrue(lm.is_iluminated(1, 1))
        self.assertTrue(lm.is_iluminated(0, 1))
        self.assertTrue(lm.is_iluminated(0, 0))

        self.assertFalse(lm.is_iluminated(0, 3))

if __name__ == '__main__':
    unittest.main()
