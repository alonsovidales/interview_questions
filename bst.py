class BSTNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

class BinarySearchTree(object):
    def __init__(self):
        self.__bst = None

    def add(self, value):
        if self.__bst is not None:
            bst = self.__bst
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
            self.__bst = BSTNode(value)

    def getByLevels(self, node=None, level=0, queues=[]):
        if not node:
            node = self.__bst

        if len(queues) <= level:
            queues.append([])
        queues[level].append(node.v)

        if node.l is not None:
            self.getByLevels(node.l, level+1, queues)
        if node.r is not None:
            self.getByLevels(node.r, level+1, queues)

        return queues

    def getByLevelsIter(self):
        levels = []
        node = self.__bst
        toVisitRight = []

        level = 0
        while node is not None:
            if len(levels) <= level:
                levels.append([])

            levels[level].append(node.v)
            if node.r is not None:
                toVisitRight.append([
                    node.r,
                    level+1
                ])

            node = node.l
            level += 1
            if node is None and len(toVisitRight) > 0:
                nodeInfo = toVisitRight.pop()
                node = nodeInfo[0]
                level = nodeInfo[1]

        return levels

bs = BinarySearchTree()
bs.add(8)
bs.add(9)
bs.add(5)
bs.add(2)
bs.add(4)
bs.add(1)

for level in bs.getByLevels():
    print ' '.join(map(str, level))

print "-- ITER --"
for level in bs.getByLevelsIter():
    print ' '.join(map(str, level))
