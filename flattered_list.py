# L1 --> L2 --> L3 --> L7 --> L8
#               |
#               v
#              L4 --> L5-->L6
# L1 --> L2 --> L3 -->L4 -->L5-->L6-->L7-->L8

class Node(object):
    def __init__(self, v, n=None, l=None):
        self.v = v
        self.n = n
        self.l = l

    def flattened(self):
        n = self
        aux = Node(0)
        root = aux
        while n != None:
            aux.n = Node(n.v)
            aux = aux.n
            if n.l != None:
                a = n.l
                while a != None:
                    aux.n = Node(a.v)
                    aux = aux.n
                    a = a.n

            n = n.n

        return root.n

    def __str__(self):
        ret = []
        a = self
        while a != None:
            ret.append(a.v)
            a = a.n

        return ' '.join(map(str, ret))

l8 = Node('L8')
l7 = Node('L7', l8)
l6 = Node('L6')
l5 = Node('L5', l6)
l4 = Node('L4', l5)

l3 = Node('L3', l7, l4)
l2 = Node('L2', l3)
l1 = Node('L1', l2)

print l1.flattened()
