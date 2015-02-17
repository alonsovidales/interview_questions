from collections import deque

class TableNode(object):
    def __init__(self):
        self.values = []
        self.childs = {}

    def append(self, k, v):
        currentNode = self
        for c in k:
            if c not in currentNode.childs:
                currentNode.childs[c] = TableNode()

            currentNode = currentNode.childs[c]

        currentNode.values.append(v)

    def get_all_childs_values(self):
        result = []
        queue = deque([self])
        while len(queue) > 0:
            current = queue.popleft()
            result += current.values
            for child in current.childs.values():
                queue.append(child)

        return result

    def __str__(self):
        return "%s - %s" % (self.values, self.childs)

class SymbolizedTable(object):
    def __init__(self):
        self.table = TableNode()

    def add(self, k, v):
        self.table.append(k, v)

    def get(self, k):
        child = self.table
        for c in k:
            if c == '?':
                break
            if c not in child.childs:
                return []
            child = child.childs[c]

        return child.get_all_childs_values()

table = SymbolizedTable()
table.add("test", "hello")
table.add("te", "hello1")
table.add("tes", "hello2")
table.add("asfgg", "hello3")
table.add("asgg", "hello4")

print table.get("te?")
print table.get("tes?")
print table.get("a?")
print table.get("asgg")
