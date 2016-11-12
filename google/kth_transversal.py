"""
You have a binary tree where each node knows the number of nodes in its sub-tree (including itself). 

Given a node n and an int k, 
write a function to return the kth 
node in an in order traversal. 
Can you do this non recursively
"""

class Bst(object):
    class Node(object):
        def __init__(self, v, l=None, r=None):
            self.v = v
            self.l = l
            self.r = r
            self.childs = 0

    def __init__(self):
        self._root = None

    def add(self, v):
        if self._root is None:
            self._root = self.Node(v)
            return

        node = self._root
        while True:
            node.childs += 1
            if node.v > v:
                if node.l is None:
                    node.l = self.Node(v)
                    return
                node = node.l
            else:
                if node.r is None:
                    node.r = self.Node(v)
                    return
                node = node.r

    def _get_inorder(self, node, p):
        if node.l is not None:
            if node.l.childs+1 < p[0]:
                p[0] -= node.l.childs+1
            else:
                v = self._get_inorder(node.l, p)
                if v is not None:
                    return v

        p[0] -= 1
        if p[0] == 0:
            return node.v

        if node.r is not None:
            v = self._get_inorder(node.r, p)
            if v is not None:
                return v

    def kth(self, p):
        if self._root is None:
            return None

        return self._get_inorder(self._root, [p])

import unittest

class TestBst(unittest.TestCase):
    def test_kth(self):
        elems = [4, 2, 6, 9, 10, 5]
        tree = Bst()
        for e in elems:
            tree.add(e)

        elems = sorted(elems)
        for i in xrange(len(elems)):
            self.assertEqual(tree.kth(i+1), elems[i])

if __name__ == '__main__':
    unittest.main()
