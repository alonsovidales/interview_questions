"""
You are given a text file that has list of dependencies between (any) two
projects in the source code repository. Write an algorithm to determine the
build order ie. which project needs to be build first, followed by which
project..based on the dependencies. 
Bonus point: If you can detect any circular dependencies and throw an exception
if found. 


EX: ProjectDependencies.txt 
a -> b (means 'a' depends on 'b'..so 'b' needs to be built first and then 'a') 
b -> c 
b -> d 
c -> d 


Then the build order can be 


d , c, b, a in that order
"""


from collections import defaultdict


class Builder(object):
	def __init__(self, deps):
		self._deps = defaultdict(list)
		self._elems = set()
		pointed_elems = set()
		for d in deps:
			self._deps[d[1]].append(d[0])
			self._elems.add(d[1])
			self._elems.add(d[0])
			pointed_elems.add(d[0])


		self._start_nodes = self._elems-pointed_elems


	def _dfs(self, node, visited_nodes, path):
		print visited_nodes, node, path
		if len(visited_nodes) == len(self._elems):
			print "Found:", path
			return True


		for elem in self._deps[node]:
			if elem not in visited_nodes:
				visited_nodes.add(elem)
				path.append(elem)
				if self._dfs(elem, visited_nodes, path):
					return True
				path.pop()
				visited_nodes.remove(elem)


		return False


	def dependencies_order(self):
		if len(self._start_nodes) == 0:
			return False


		(elem, ) = self._start_nodes
		path = [elem]
		if self._dfs(elem, set(elem), path):
			return tuple(path)
	
		return False


import unittest


class TestBuilder(unittest.TestCase):
	def test_dependencies_order(self):
		bl = Builder((
			('a', 'b'),
			('b', 'c'),
			('b', 'd'),
			('c', 'd'),
))
		self.assertEquals(bl.dependencies_order(), ('d' , 'c', 'b', 'a',))


		bl = Builder((
			('a', 'b'),
			('b', 'a'),
			('b', 'd'),
			('c', 'd'),
))
		self.assertFalse(bl.dependencies_order())


if __name__ == '__main__':
	unittest.main()
