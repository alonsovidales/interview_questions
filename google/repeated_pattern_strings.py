"""
Given a string (1-d array) , find if there is any sub-sequence that repeats itself. 
Here, sub-sequence can be a non-contiguous pattern, with the same relative order. 

Eg: 
    1. abab <------yes, ab is repeated 
    2. abba <---- No, a and b follow different order 
    3. acbdaghfb <-------- yes there is a followed by b at two places 
    4. abcdacb <----- yes a followed by b twice 

    The above should be applicable to ANY TWO (or every two) characters in the string and optimum over time. 

    In the sense, it should be checked for every pair of characters in the string.
"""

class Patterns(object):
    def is_pattern(self, string):
        substrings = {}
        for i in xrange(len(string)):
            patterns_to_add = {}
            for j in  xrange(i+1, len(string)):
                pattern = (string[i], string[j])
                if pattern in substrings and substrings[pattern] != j:
                    return True

                if pattern not in patterns_to_add:
                    patterns_to_add[pattern] = j

            substrings.update(patterns_to_add)

        return False


import unittest

class TestPatterns(unittest.TestCase):
    def test_is_pattern(self):
        pt = Patterns()
        self.assertTrue(pt.is_pattern('abab'))
        self.assertFalse(pt.is_pattern('abba'))
        self.assertTrue(pt.is_pattern('acbdaghfb'))
        self.assertTrue(pt.is_pattern('abcdacb'))
        self.assertFalse(pt.is_pattern(''))

if __name__ == '__main__':
    unittest.main()
