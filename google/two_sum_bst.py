"""
Given a BST and a number x, check whether exists two nodes in the BST whose sum
equals to x. You can not use one extra array to serialize the BST and do a 2sum
solver on it.
"""

class Bst(object):
    class BstNode(object):
        def __init__(self, v, l=None, r=None):
            self.v = v
            self.l = l
            self.r = r

    def __init__(self):
        self._tree = None

    def add(self, v):
        if self._tree is None:
            self._tree = self.BstNode(v)
        else:
            tree = self._tree
            while True:
                if tree.v > v:
                    if tree.l is not None:
                        tree = tree.l
                    else:
                        tree.l = self.BstNode(v)
                        return
                else:
                    if tree.r is not None:
                        tree = tree.r
                    else:
                        tree.r = self.BstNode(v)
                        return

    def exists(self, v, x=None, node=None):
        if node is None:
            node = self._tree

        if node.v == v and v != x:
            return True

        if v > node.v:
            return node.r is not None and self.exists(v, x, node.r)
        else:
            return node.l is not None and self.exists(v, x, node.l)

    def two_sum(self, x, node=None):
        if node is None:
            node = self._tree

        if self.exists(x-node.v, node.v):
            return True

        return ((node.r is not None and self.two_sum(x, node.r)) or
               (node.l is not None and self.two_sum(x, node.l)))

import unittest

class TestBst(unittest.TestCase):
    def test_two_sum(self):
        bst = Bst()
        bst.add(4)
        bst.add(3)
        bst.add(5)
        bst.add(8)
        bst.add(1)
        self.assertTrue(bst.two_sum(6))
        self.assertTrue(bst.two_sum(8))
        self.assertFalse(bst.two_sum(2))
        self.assertFalse(bst.two_sum(1))

if __name__ == '__main__':
    unittest.main()
