from collections import defaultdict

class Graph(object):
    def __init__(self, edges):
        self._gr_from_to = defaultdict(set)
        self._gr_to_from = defaultdict(set)

        for e in edges:
            self._gr_from_to[e[0]].add(e[1])
            self._gr_to_from[e[1]].add(e[0])
    
    def topological_order(self):
        order = []
        vertices = set(self._gr_from_to.keys()) - set(self._gr_to_from.keys())

        while len(vertices) > 0:
            v_from = vertices.pop()
            order.append(v_from)
            for v_to in self._gr_from_to[v_from]:
                self._gr_to_from[v_to].discard(v_from)
                if len(self._gr_to_from[v_to]) == 0:
                    vertices.add(v_to)
                    del(self._gr_to_from[v_to])

        # We have a cicle
        if len(self._gr_to_from):
            return None

        return order

if __name__ == '__main__':
    gr = Graph((
        (5, 11),
        (11, 2),
        (7, 11),
        (7, 8),
        (11, 9),
        (11, 10),
        (8, 9),
        (3, 8),
        (3, 10),
    ))
    print gr.topological_order()

    gr = Graph((
        (5, 11),
        (11, 5),
        (11, 2),
        (7, 11),
        (7, 8),
        (11, 9),
        (11, 10),
        (8, 9),
        (3, 8),
        (3, 10),
    ))
    print gr.topological_order()
