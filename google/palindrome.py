"""
Given a string S, you are allowed to convert it to a palindrome by adding 0 or
more characters in front of it. 
Find the length of the shortest palindrome that you can create from S by
applying the above transformation.
"""

def is_palindrome(string):
    for i in xrange(len(string)):
        if string[i] != string[len(string)-i-1]:
            return False

    return True

def how_to_palindrome(string):
    for i in xrange(len(string)):
        if is_palindrome(string[len(string)-i:][::-1] + string):
            return i

    return 0

import unittest

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(how_to_palindrome('yuyt'), 1)
        self.assertEqual(how_to_palindrome('yuuyt'), 1)
        self.assertEqual(how_to_palindrome('uyt'), 2)
        self.assertEqual(how_to_palindrome(''), 0)
        self.assertEqual(how_to_palindrome('a'), 0)
        self.assertEqual(how_to_palindrome('aa'), 0)

if __name__ == '__main__':
    unittest.main()
