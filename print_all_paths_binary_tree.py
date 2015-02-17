class TreeNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = r
        self.r = l

    def get_paths(self, path=[]):
        result = []
        new_path = path[:]
        new_path.append(self.v)
        if self.l is None and self.r is None:
            return [new_path]

        if self.l != None:
            result += self.l.get_paths(new_path)
        if self.r != None:
            result += self.r.get_paths(new_path)

        return result

#     4
#     /\
#    3  6
#   /\  /\
#  8 9 7  2
# /   \
#1     0
a1 = TreeNode(1)
a8 = TreeNode(8, a1)
a0 = TreeNode(0)
a9 = TreeNode(9, r=a0)
a3 = TreeNode(3, a8, a9)

a7 = TreeNode(7)
a2 = TreeNode(2)
a6 = TreeNode(6, a7, a2)
root = TreeNode(4, a3, a6)

print root.get_paths()
