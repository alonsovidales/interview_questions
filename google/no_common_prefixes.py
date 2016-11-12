"""
Use the shorest unique prefix to represent each word in the array 
input: ["zebra", "dog", "duck","dot"] 
output: {zebra: z, dog: do, duck: du} 

[zebra, dog, duck, dove] 
{zebra:z, dog: dog, duck: du, dove: dov} 

[bearcat, bear] 
{bearcat: bearc, bear: ""}
"""

class PrefixFinder(object):
    def __init__(self, words):
        # Remove all the duplicated words
        self._words = set(words)

    def find(self):
        prefixes = {}
        to_delete = set([])
        for w in self._words:
            for i in xrange(len(w)):
                if w[:i+1] in prefixes:
                    to_delete.add(w[:i+1])
                    coll_word = prefixes[w[:i+1]]
                    prefixes[coll_word[:i+2]] = coll_word
                else:
                    prefixes[w[:i+1]] = w
                    break

        return {v: k for k, v in prefixes.items() if k not in to_delete}

import unittest

class TestPrefixFinder(unittest.TestCase):
    def test_find(self):
        pf = PrefixFinder(['zebra', 'dog', 'duck', 'dove'])
        self.assertEqual(
            pf.find(),
            {'zebra': 'z', 'dog': 'dog', 'duck': 'du', 'dove': 'dov'}
        )

        pf = PrefixFinder([])
        self.assertEqual(
            pf.find(),
            {}
        )

        pf = PrefixFinder(['dog', 'dog'])
        self.assertEqual(
            pf.find(),
            {'dog': 'd'}
        )

if __name__ == '__main__':
    unittest.main()
