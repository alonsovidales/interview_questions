"""
Boggle game - given a board of letters (2d array) and a word (string), return
whether the word exists in the board. From each letter you can move in all
directions (including diagonals), but you cannot use the same letter twice.  
"""

class SearchInBoard:
	def __init__(self, board):
		self._board = board

	def _search_str_from(self, str_to_find, x, y):
		if str_to_find == '':
			return True

		if len(str_to_find) == 0 or str_to_find[0] != self._board[x][y]:
			return False

		found = False
		if x < len(self._board)-1:
			found = self._search_str_from(str_to_find[1:], x+1, y)

		if not found and y < len(self._board[0])-1:
			found = self._search_str_from(str_to_find[1:], x, y+1)

		if not found and x > 0:
			found = self._search_str_from(str_to_find[1:], x-1, y)

		if not found and y > 0:
			found = self._search_str_from(str_to_find[1:], x, y-1)

		return found

	def search_str(self, str_to_find):
		for x in xrange(len(self._board)):
			for y in xrange(len(self._board[x])):
				if self._search_str_from(str_to_find, x, y):
					return True

		return False

board_search = SearchInBoard([
	['t', 'd', 'f', 'g', 'r', 'q', 'w'],
	['t', 'h', 'f', 'g', 'r', 'q', 'w'],
	['t', 'h', 'f', 'g', 'r', 't', 'w'],
	['t', 'u', 's', 'g', 'r', 'h', 'i'],
	['t', 'i', 'f', 'g', 'r', 'q', 's'],
	['t', 'd', 'f', 'g', 'r', 'q', 'w'],
	['t', 'd', 'f', 'g', 'r', 'q', 'w'],
	['t', 'd', 'f', 'g', 'r', 'q', 'w'],
	['t', 'd', 'f', 'g', 'r', 'q', 'w'],
	['t', 'd', 'f', 'g', 'r', 'q', 'w'],
	['t', 'd', 'f', 'g', 'r', 'q', 'w'],
])
print board_search.search_str('this')
