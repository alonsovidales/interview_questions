"""
There is an array of 3-tuple, in the form of (a, 1, 5). The first element in
the tuple is the id, the second and third elements are both integers, and the
third is always larger than or equal to the second. Assume that the array is
sorted based on the second element of the tuple. Write a function that breaks
each of the 3-tuple into two 2-tuples like (a, 1) and (a, 5), and sort them
according to the integer. 

E.g. given (a, 1, 5), (b, 2, 4), (c, 7, 8), output (a, 1), (b, 2), (b, 4), (a, 5), (c, 7), (c, 8).
"""

def break_tupples(tuples):
    sorted_tuples = []
    unsorted_tuples = []
    for tup in tuples:
        sorted_tuples.append((tup[0], tup[1]))
        unsorted_tuples.append((tup[0], tup[2]))

    unsorted_tuples = sorted(unsorted_tuples, key=lambda x: x[1])

    result = []
    i1 = 0
    i2 = 0
    for i in xrange(len(sorted_tuples) + len(unsorted_tuples)):
        if i1 >= len(sorted_tuples) or sorted_tuples[i1][1] > unsorted_tuples[i2][1]:
            result.append(unsorted_tuples[i2])
            i2 += 1
        else:
            result.append(sorted_tuples[i1])
            i1 += 1

    return tuple(result)


import unittest

class TestTuples(unittest.TestCase):
    def test_break_tuples(self):
        self.assertEquals(break_tupples((
            ('a', 1, 5),
            ('b', 2, 4),
            ('c', 7, 8),
        )), (
            ('a', 1),
            ('b', 2),
            ('b', 4),
            ('a', 5),
            ('c', 7),
            ('c', 8),
        ))

if __name__ == '__main__':
    unittest.main()
