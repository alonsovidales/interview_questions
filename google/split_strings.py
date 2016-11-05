"""
Given a string "2-4a0r7-4k", there are two dashes which we can split into 3 groups of length 1, 5, 2. 

If we want each group to be length 4, then we get "24A0-R74k" 

Given a String A and an int K, return a correctly formatted string. 

IF A is "2-4A0r7-4k" and B is 4, string is "24A0-R74K" 
IF K is 3, string is "24-A0R-74K" as the first grp could be shorter.
"""

def split_string(string, segment_size):
    aux_str = string.replace('-', '').upper()
    first_elem_len = len(aux_str) % segment_size

    result = [aux_str[:first_elem_len]] if first_elem_len != 0 else []

    for i in xrange(len(aux_str) / segment_size):
        init_pos = first_elem_len + (i * segment_size)
        result.append(aux_str[init_pos:init_pos+segment_size])

    return '-'.join(result)

import unittest

class TestSplitStrings(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split_string('2-4a0r7-4k', 4), '24A0-R74K')
        self.assertEqual(split_string('2-4A0r7-4k', 3), '24-A0R-74K')

if __name__ == '__main__':
    unittest.main()
