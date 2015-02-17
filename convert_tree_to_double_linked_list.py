from collections import deque

class LinkedListNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        if l is None and r is None:
            self.l = self
            self.r = self
        else:
            self.l = l
            self.r = r

    def append_left(self, v):
        new = LinkedListNode(v, self.l, self)
        self.l.r = new
        self.l = new

    def __str__(self):
        ret = [self.v]
        aux = self.r
        while aux != self:
            ret.append(aux.v)
            aux = aux.r

        return ':'.join(map(str, ret))
            

class TreeNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

    def get_as_double_linked_list(self):
        queue = deque([self])
        linked_list = None

        while len(queue) > 0:
            current = queue.popleft()
            if linked_list is None:
                linked_list = LinkedListNode(self.v)
            else:
                linked_list.append_left(current.v)

            if current.l != None:
                queue.append(current.l)
            if current.r != None:
                queue.append(current.r)

        return linked_list

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
a1 = TreeNode(1, r=a5)
a6 = TreeNode(6)
a2 = TreeNode(2, a1, a6)

root = TreeNode(4, a2, a3)

print root.get_as_double_linked_list()
