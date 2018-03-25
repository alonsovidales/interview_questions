"""
Given a start position and an target position on the grid. You can move up,down,left,right from one node to another adjacent one on the grid. However there are some walls on the grid that you cannot pass. Now find the shortest path from the start to the target. 
"""


from collections import defaultdict


class Game(object):
	def __init__(self, grid):
		self._grid = grid


	def _is_possible_and_better(self, distances, f, t):
		return (
                    t[0] >= 0 and t[0] < len(self._grid) and
                    t[1] >=0 and t[1] < len(self._grid[0]) and
                    self._grid[t[0]][t[1]] != 1 and
                    distances.get(t, float('inf')) > distances[f]+1)


	def get_sortest_path(self, f, t):
		stack = [f]
		distances = defaultdict(int)
		distances[f] = 0
		while len(stack) > 0:
                    curr = stack.pop()
                    possible = (curr[0]-1, curr[1])
                    if self._is_possible_and_better(distances, curr, possible):
                        distances[possible] = distances[curr]+1
                        stack.append(possible)


                    possible = (curr[0]+1, curr[1])
                    if self._is_possible_and_better(distances, curr, possible):
                        distances[possible] = distances[curr]+1
                        stack.append(possible)


                    possible = (curr[0], curr[1]+1)
                    if self._is_possible_and_better(distances, curr, possible):
                        distances[possible] = distances[curr]+1
                        stack.append(possible)


                    possible = (curr[0], curr[1]-1)
                    if self._is_possible_and_better(distances, curr, possible):
                        distances[possible] = distances[curr]+1
                        stack.append(possible)


		return distances.get(t, -1)


import unittest


class TestGame(unittest.TestCase):
	def test_get_sortest_path(self):
		gm = Game((
			(0, 1, 0, 1, 0, 0),
			(0, 1, 0, 1, 1, 0),
			(0, 1, 0, 0, 0, 1),
			(1, 0, 1, 1, 0, 0),
			(0, 0, 0, 0, 0, 0),
			(0, 0, 0, 0, 0, 0),
))
		self.assertEqual(gm.get_sortest_path((0, 0), (2, 2)), -1)
		self.assertEqual(gm.get_sortest_path((0, 0), (2, 0)), 2)
		self.assertEqual(gm.get_sortest_path((0, 2), (5, 4)), 7)


if __name__ == '__main__':
	unittest.main()
