# Create a function to calculate the height of an n-ary tree.

class NAryTreeNode(object):
    def __init__(self, value, childs=[]):
        self.v = value
        self.childs = childs

    def get_height(self):
        max_h = 0
        for child in self.childs:
            child_h = child.get_height()
            if child_h > max_h:
                max_h = child_h

        return 1 + max_h

import unittest

class TestNAryTree(unittest.TestCase):
    def test_height(self):
        tree = NAryTreeNode(1, [
            NAryTreeNode(2, [
                NAryTreeNode(3, []),
                NAryTreeNode(4, []),
                NAryTreeNode(5, []),
            ]),
            NAryTreeNode(2, []),
            NAryTreeNode(3, []),
        ])
        self.assertEqual(tree.get_height(), 3)
        self.assertEqual(tree.childs[0].get_height(), 2)
        self.assertEqual(tree.childs[2].get_height(), 1)

if __name__ == '__main__':
    unittest.main()
