from collections import deque

class TreeNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

    def pre_order(self, add_null=False):
        result = [self.v]
        if self.l is not None:
            result += self.l.pre_order(add_null)
        elif add_null:
            result.append('#')
            
        if self.r is not None:
            result += self.r.pre_order(add_null)
        elif add_null:
            result.append('#')

        return result

    def in_order(self):
        result = []
        if self.l is not None:
            result += self.l.in_order()
        result.append(self.v)
        if self.r is not None:
            result += self.r.in_order()

        return result

    def post_order(self):
        result = []
        if self.l is not None:
            result += self.l.post_order()
        if self.r is not None:
            result += self.r.post_order()
        result.append(self.v)

        return result

    def level_order(self):
        result = []
        queue = deque([self])
        while len(queue) > 0:
            current = queue.popleft()
            result.append(current.v)
            if current.l is not None:
                queue.append(current.l)
            if current.r is not None:
                queue.append(current.r)

        return result

    def by_levels(self):
        result = []
        queue = deque([(self, 0)])
        while len(queue) > 0:
            n = queue.popleft()
            current = n[0]
            deep = n[1]
            if len(result) <= deep:
                result.append([])
            result[deep].append(current.v)
            if current.l is not None:
                queue.append((current.l, deep+1))
            if current.r is not None:
                queue.append((current.r, deep+1))

        return result

    def serialize(self):
        return ' '.join(map(str, root.pre_order(True)))

def _deserialize(parts, pos):
    if len(parts) == 0:
        return None

    pos[0] += 1
    if parts[pos[0]-1] != '#':
        tree = TreeNode(parts[0])
        tree.l = _deserialize(parts, pos)
        tree.r = _deserialize(parts, pos)

        return tree

def deserialize(string):
    parts = string.split()
    return _deserialize(parts, [0])

#         4
#        /\
#       2  3
#      /\  /\
#     1  67  9
#    /     \
#   5       10

a10 = TreeNode(10)
a7 = TreeNode(7, r=a10)
a9 = TreeNode(9)
a3 = TreeNode(3, a7, a9)

a5 = TreeNode(5)
a1 = TreeNode(1, l=a5)
a6 = TreeNode(6)
a2 = TreeNode(2, a1, a6)

root = TreeNode(4, a2, a3)

print "Pre:", root.pre_order()
print "In:", root.in_order()
print "Post:", root.post_order()
print "Level:", root.level_order()
print "By Level:", root.by_levels()
print "Serialize  :", root.serialize()
print "Deserialize:", deserialize(root.serialize()).serialize()
