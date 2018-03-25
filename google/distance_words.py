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
        self._dist = distances
        self._total_words = len(distances)

    def _get_min_distance(self, pos, min_distance):
        min_pos = pos
        for i in xrange(len(pos)):
            aux_pos = pos[:]
            aux_pos[i] += 1
            if aux_pos [i] >= self._total_words:
                continue

            words_pos = [self._dist[i][aux_pos[i]] for i in xrange(len(self._dist))]
            dist = max(words_pos) - min(words_pos)

            if dist < min_distance[1]:
                min_distance[1] = dist
                min_distance[0] = words_pos

            self._get_min_distance(aux_pos, min_distance)

        return min_distance[0]

    def min_distance(self):
        init_pos = [0] * len(self._dist)
        words_pos = [self._dist[i][init_pos[i]] for i in xrange(len(self._dist))]
        dist = max(words_pos) - min(words_pos)

        min_distance = [words_pos, dist]

        return self._get_min_distance(init_pos, min_distance)

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
