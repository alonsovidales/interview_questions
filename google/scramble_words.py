# You are given a scrambled input sentence. Each word is scrambled independently, and the results are concatenated. So: 
#   'hello to the world' 
# might become: 
#   'elhloothtedrowl' 
# You have a dictionary with all words in it. Unscramble the sentence.

class Scramble(object):
    def __init__(self, dictionary):
        self._dict = {}
        for w in dictionary:
            self._dict[''.join(sorted(w))] = w

    def unescramble(self, sentence):
        result = []
        from_pos = 0
        for i in xrange(len(sentence)+1):
            sorted_str = ''.join(sorted(sentence[from_pos:i]))
            if ''.join(sorted_str) in self._dict:
                result.append(self._dict[sorted_str])
                from_pos = i

        return ' '.join(result)

import unittest

class TestUnescramble(unittest.TestCase):
    def test_unescramble(self):
        sc = Scramble((
            'aaaa',
            'bbbbbbb',
            'hello',
            'to',
            'the',
            'world'
        ))

        self.assertEqual(sc.unescramble('elhloothtedrowl'), 'hello to the world')
        self.assertEqual(sc.unescramble(''), '')
        self.assertEqual(sc.unescramble('aaaa'), 'aaaa')

if __name__ == '__main__':
    unittest.main()
