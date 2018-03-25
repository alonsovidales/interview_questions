"""
Given 'n' circles (each defined by center and radius) 

Write an algorithm to detect if circles intersect with any other circle in the
same plane 

Better than O(n^2) complexity
"""

import math

class CirclesField(object):
    def _get_distance(self, x, y):
        return math.sqrt(
            math.pow(abs(x[0]-y[0]), 2)+
            math.pow(abs(x[1]-y[1]), 2)
        )

    def get_intersect(self, c1, c2):
        return self._get_distance(c1, c2) <= c1[2]+c2[2]

import unittest

class TestCirclesField(unittest.TestCase):
    def test_get_intersect(self):
        ci = CirclesField()
        self.assertTrue(ci.get_intersect(
            (1, 1, 0.5),
            (1, 2, 0.5)
        ))

        self.assertFalse(ci.get_intersect(
            (1, 1, 0.25),
            (1, 2, 0.5)
        ))

if __name__ == '__main__':
    unittest.main()
