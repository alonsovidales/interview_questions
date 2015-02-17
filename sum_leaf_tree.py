class TreeNode(object):
    def __init__(self, value):
        self.childs = []
        self.value = value

    def append_child(self, node):
        self.childs.append(node)

    def get_childs_sum(self, v=0):
        result = []
        if len(self.childs) == 0:
            return [v+self.value]

        for c in self.childs:
            result += c.get_childs_sum(v+self.value)

        return result

tree = TreeNode(0)

aux = TreeNode(1)
aux.append_child(TreeNode(2))
aux.append_child(TreeNode(3))
tree.append_child(aux)

aux = TreeNode(6)
aux.append_child(TreeNode(4))
aux.append_child(TreeNode(5))
tree.append_child(aux)

tree.append_child(TreeNode(7))

print "Result: %s" % tree.get_childs_sum()
