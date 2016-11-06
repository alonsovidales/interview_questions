"""
Given a undirected graph with weights, return the sum of the weight of each
path between two nodes (shortest path between two vertices). Assume there are
no cycles. 

Example:
    Input:
        A
        | 1
        B
    2 /   \ 3
    C       D

Output:
18
since 
A to B has weight 1
A to C has weight 3
A to D has weight 4
B to C has weight 2
B to D has weight 3
C to D has weight 5
"""

from collections import defaultdict

class Graph(object):
    def __init__(self, graph):
        self._gr = defaultdict(dict)
        for v in graph:
            self._gr[v[0]][v[1]] = v[2]
            self._gr[v[1]][v[0]] = v[2]

    def sum_weights(self):
        weights = {}
        used_v = 0
        for v in self._gr.keys():
            # We can ignore the last of the vertices
            if used_v+1 == len(self._gr):
                break

            used_v += 1

            known_distances = {
                v: 0,
            }
            to_visit = [v]
            while len(to_visit) > 0:
                curr_v = to_visit.pop()
                curr_w = known_distances[curr_v]
                for dest, w in self._gr[curr_v].items():
                    if dest not in known_distances or known_distances[dest] > curr_w + w:
                        known_distances[dest] = curr_w + w
                        to_visit.append(dest)

            for to, w in known_distances.items():
                if w > 0:
                    if v > to:
                        weights[(v, to)] = w
                    else:
                        weights[(to, v)] = w

        total = 0
        for w in weights.values():
            total += w

        return total

import unittest

class TestGraph(unittest.TestCase):
    def test_sum_weights(self):
        gr = Graph((
            ('a', 'b', 1),
            ('b', 'c', 2),
            ('b', 'd', 3),
        ))

        self.assertEqual(gr.sum_weights(), 18)

if __name__ == '__main__':
    unittest.main()
