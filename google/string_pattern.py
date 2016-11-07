"""
Question was "Given a pattern and a string input - find if the string follows the same pattern and return 0 or 1. 
Examples: 
    1) Pattern : "abba", input: "redbluebluered" should return 1. 
    2) Pattern: "aaaa", input: "asdasdasdasd" should return 1. 
    3) Pattern: "aabb", input: "xyzabcxzyabc" should return 0. 

"""

from collections import defaultdict

class PatternMatching(object):
    def match(self, string, pattern, dictionary={}):
        if len(string) == 0 and len(pattern) == 0:
            return True

        if len(string) == 0 or len(pattern) == 0:
            return False

        if pattern[0] in dictionary:
            char_str = dictionary[pattern[0]]
            if string[:len(char_str)] == char_str:
                return self.match(string[len(char_str):], pattern[1:], dictionary)
        else:
            for i in xrange(1, len(string)):
                aux_dict = dictionary.copy()
                aux_dict[pattern[0]] = string[:i]
                if self.match(string[i:], pattern[1:], aux_dict):
                    return True

        return False

import unittest

class TestPatternMatching(unittest.TestCase):
    def test_match(self):
        pm = PatternMatching()
        self.assertTrue(pm.match('redbluebluered', 'abba'))

        pm = PatternMatching()
        self.assertTrue(pm.match('asdasdasdasd', 'aaaa'))

        pm = PatternMatching()
        self.assertFalse(pm.match('xyzabcxzyabc', 'aabb'))

if __name__ == '__main__':
    unittest.main()
