"""
Given a Pattern and a dictionary, print out all the strings that match the pattern. 
where a character in the pattern is mapped uniquely to a character in the
dictionary ( this is what i was given first). 

e.g 1. ("abc" , <"cdf", "too", "hgfdt" ,"paa">) -> output = "cdf" 
2. ("acc" , <"cdf", "too", "hgfdt" ,"paa">) -> output = "too", "paa"
"""

from collections import defaultdict

class Dictionary(object):
    def __init__(self, dictionary):
        self._dict = defaultdict(list)
        for w in dictionary:
            self._dict[self._get_key(w)].append(w)

    def find(self, w):
        return self._dict[self._get_key(w)]

    def _get_key(self, string):
        known_chars = {}
        key = []
        char = 'a'
        for c in string:
            if c in known_chars:
                key.append(known_chars[c])
            else:
                known_chars[c] = char
                key.append(char)
                char = chr(ord(char)+1)


        return ''.join(key)

import unittest

class TestPatterFinder(unittest.TestCase):
    def test_find_pattern(self):
        dic = Dictionary(("cdf", "too", "hgfdt" ,"paa"))
        self.assertEqual(dic.find('abc'), ["cdf"])

        dic = Dictionary(("cdf", "too", "hgfdt" ,"paa"))
        self.assertEqual(dic.find('acc'), ["too", "paa"])

if __name__ == '__main__':
    unittest.main()
