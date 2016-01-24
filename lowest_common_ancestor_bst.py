class BSTNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

class BinarySearchTree(object):
    def __init__(self):
        self._bst = None

    def add(self, value):
        if self._bst is not None:
            bst = self._bst
            prev = bst
            while bst is not None:
                prev = bst
                if bst.v < value:
                    bst = bst.r
                else:
                    bst = bst.l
            if prev.v < value:
                prev.r = BSTNode(value)
            else:
                prev.l = BSTNode(value)
        else:
            self._bst = BSTNode(value)

    def getByLevels(self, node=None, level=0, queues=[]):
        if not node:
            node = self._bst

        if len(queues) <= level:
            queues.append([])
        queues[level].append(node.v)

        if node.l is not None:
            self.getByLevels(node.l, level+1, queues)
        if node.r is not None:
            self.getByLevels(node.r, level+1, queues)

        return queues

    def lowest_common_ancestor(self, min_num, max_num, current_node = None, deep=0, lca_max_deep=None, searching=None, lca=None, found_max=None):
            # Go in inorder trying to find the min num, when found until find
            # the max, go getting the min deep of the level and the value, this
            # will be the lca
            if current_node is None:
                    current_node = self._bst
                    searching = [False]
                    lca_max_deep = [0]
                    lca = [None]
                    found_max = [False]

            if current_node.l is not None:
                    self.lowest_common_ancestor(min_num, max_num, current_node.l, deep+1, lca_max_deep, searching, lca, found_max)

            if not found_max[0]:
                if not searching[0]:
                    if current_node.v == min_num:
                        print "Found min:", current_node.v
                        searching[0] = True
                        lca_max_deep[0] = deep
                else:
                    if lca_max_deep[0] > deep:
                        print "Deep:", deep, current_node.v
                        lca_max_deep[0] = deep
                        lca[0] = current_node.v
                if current_node.v == max_num:
                    print "Found max:", current_node.v
                    found_max[0] = True

            if current_node.r is not None and not found_max[0]:
                    self.lowest_common_ancestor(min_num, max_num, current_node.r, deep+1, lca_max_deep, searching, lca, found_max)

            return lca[0]

bs = BinarySearchTree()
bs.add(8)
bs.add(9)
bs.add(3)
bs.add(2)
bs.add(4)
bs.add(5)

for level in bs.getByLevels():
    print ' '.join(map(str, level))

print bs.lowest_common_ancestor(2, 5)
print "---- ----"
print bs.lowest_common_ancestor(2, 9)
