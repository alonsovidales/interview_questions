"""
Find the shortest path between a start node and end node in a undirected +ve weighted graph. 
You are allowed to add at max one edge between any two nodes which are not directly connected to each other. 
ex: 

    From | To | Weight 
    1 2 2 
    1 4 4 
    2 3 1 
    3 4 3 
    4 5 1 

    start node = 1, end node = 5. 
    extra edge weight = 2.
"""

class UnidrectedGraph(object):
    def __init__(self, graph_def):
        self._graph = {}
        self._vetices = set()
        for edge in graph_def:
            dest = (edge[0], edge[2])
            self._vetices.add(edge[0])
            self._vetices.add(edge[1])
            if edge[1] in self._graph:
                self._graph[edge[1]].append(dest)
            else:
                self._graph[edge[1]] = [dest]

            dest = (edge[1], edge[2])
            if edge[0] in self._graph:
                self._graph[edge[0]].append(dest)
            else:
                self._graph[edge[0]] = [dest]

        print self._graph

    def sortest_path_extra_vertex(self, from_v, to_v, extra_weight):
        distances = {from_v: 0}
        q = [from_v]
        while len(q) > 0:
            v = q.pop()
            conected_v = set()
            for t, w in self._graph.get(v, []):
                conected_v.add(t)
                if distances[v] + w < distances.get(t, float('inf')):
                    distances[t] = distances[v] + w
                    q.append(t)

            for t in self._vetices - conected_v:
                if distances[v] + extra_weight < distances.get(t, float('inf')):
                    distances[t] = distances[v] + extra_weight
                    q.append(t)

        return distances[to_v]

import unittest

class TestUnidrectedGraph(unittest.TestCase):
    def test_sortest_path_extra_vertex(self):
        ug = UnidrectedGraph((
            (1, 2, 2),
            (1, 4, 4),
            (2, 3, 1),
            (3, 4, 3),
            (4, 5, 1),
        ))
        self.assertEqual(ug.sortest_path_extra_vertex(1, 5, 2), 2)

        ug = UnidrectedGraph((
            (1, 2, 2),
            (1, 5, 8),
            (1, 4, 4),
            (2, 3, 1),
            (3, 4, 3),
            (4, 5, 1),
        ))
        self.assertEqual(ug.sortest_path_extra_vertex(1, 5, 2), 4)

if __name__ == '__main__':
    unittest.main()
