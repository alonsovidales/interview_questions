# find the kth smallest element of a BST.

class BSTNode(object):
	def __init__(self, v, l=None, r=None):
		self.v = v
		self.l = l
		self.r = r

class BSTTree(object):
	def __init__(self):
		self._bst = None

	def add(self, value):
		if self._bst is None:
			self._bst = BSTNode(value)
			return

		prev_node = self._bst
		curr_node = self._bst
		while curr_node is not None:
			prev_node = curr_node
			if curr_node.v > value:
				curr_node = curr_node.l
			else:
				curr_node = curr_node.r

		if prev_node.v > value:
			prev_node.l = BSTNode(value)
		else:
			prev_node.r = BSTNode(value)

	def get_kth_smallest(self, kth, node=None, last_elemts=None):
		if node is None:
			node = self._bst
			last_elemts=[0]

		result = None
		if node.l is not None:
			result = self.get_kth_smallest(kth, node.l, last_elemts)

		last_elemts[0] += 1
		if last_elemts[0] == kth:
			result = node.v
		elif node.r is not None and last_elemts[0] < kth:
			result = self.get_kth_smallest(kth, node.r, last_elemts)

		return result

tree = BSTTree()
tree.add(8)
tree.add(9)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(2)
print tree.get_kth_smallest(1)
