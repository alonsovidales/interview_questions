from collections import deque

class BST(object):
    def __init__(self, v):
        self.v = v
        self.w_l = 0
        self.w_r = 0
        self.l = None
        self.r = None

    def add(self, v):
        aux = self
        while aux is not None:
            if v < aux.v:
                aux.w_l += 1
                if aux.l is None:
                    aux.l = BST(v)
                    return

                aux = aux.l
            else:
                aux.w_r += 1
                if aux.r is None:
                    aux.r = BST(v)
                    return

                aux = aux.r

    def print_by_levels(self):
        result = []
        queue = deque([(self, 0)])
        while len(queue) > 0:
            aux = queue.popleft()
            if len(result) <= aux[1]:
                result.append([])

            result[aux[1]].append((aux[0].v, aux[0].w_l, aux[0].w_r))
            if aux[0].l is not None:
                queue.append((aux[0].l, aux[1]+1))

            if aux[0].r is not None:
                queue.append((aux[0].r, aux[1]+1))

        return result

    def get_by_pos(self, pos):
        current_w = 0
        aux = self
        while aux is not None and current_w + aux.w_l + 1 != pos:
            if current_w + aux.w_l >= pos:
                aux = aux.l
            else:
                current_w += aux.w_l + 1
                aux = aux.r

        if aux is None:
            return None

        return aux.v

#       10
#       /\
#      6  15
#    /    /
#   4    12
#  /\     \
# 2  5     14

root = BST(10)
root.add(6)
root.add(15)
root.add(12)
root.add(14)
root.add(4)
root.add(2)
root.add(5)

print root.print_by_levels()
print root.get_by_pos(3)
print root.get_by_pos(2)
print root.get_by_pos(1)
print root.get_by_pos(4)
print root.get_by_pos(6)
print root.get_by_pos(7)
print root.get_by_pos(8)
print root.get_by_pos(9)
