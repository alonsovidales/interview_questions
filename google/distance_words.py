"""
We have words and there positions in a paragraph in sorted order. Write an
algorithm to find the least distance for a given 3 words. 
eg. for 3 words 
job: 5, 9 , 17 
in: 4, 13, 18 
google: 8, 19, 21 
... 
... 
Answer: 17, 18, 19 
Can you extend it to "n" words? 

Context: In Google search results, the search terms are highlighted in the
short paragraph that shows up. We need to find the shortest sentence that has
all the words if we have word positions as mentioned above.
"""

class WordsHelper(object):
    def __init__(self, distances):
        self._distances = distances
        self._words_per_distance = len(distances[0])

    def _get_min_distance(self, pos, min_distance):
        for d in xrange(len(self._distances)):
            aux_pos = pos[:]

            distance = 0
            for i in xrange(self._words_per_distance):
                print self._distances[i], aux_pos[i]
                distance += self._distances[i][aux_pos[i]]

            if distance < min_distance:
                min_distance = min_distance

            aux_pos[d] += 1
            if aux_pos[d] >= self._words_per_distance:
                continue

            dist = self._get_min_distance(aux_pos, min_distance)

        return min_distance

    def min_distance(self):
        pos = [0] * len(self._distances)
        self._get_min_distance(pos, float('inf'))

import unittest

class TestWordsHelper(unittest.TestCase):
    def test_min_distance(self):
        wh = WordsHelper((
            (5, 9 , 17),
            (4, 13, 18),
            (8, 19, 21)
        ))
        self.assertEqual(wh.min_distance(), [17, 18, 19])

if __name__ == '__main__':
    unittest.main()
