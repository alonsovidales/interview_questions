"""
You are given a list of items / combo_items with their price list. 
And you are given a list of items to buy. 
Now you are asked to find which combination to buy so that it costs you minimum. 
It doesn't matter if you are getting some extra items if it costs less. 




Sr.No Price | Items/Combo_Items 
1.	5	|	Burger 
2.	4	|	French_Frice 
3.	8	|	Coldrink 
4.	12	|	Burger, French_Frice, Coldrink 
5.	14 | Burger, Coldrink 




Input Items to Buy: 
Coldrink 


Output(Sr.No) 
3 


Input Items to Buy: 
Burger Coldrink 


Output(Sr.No) 
4 


Input Items to Buy: 
Burger French_Frice 


Output(Sr.No) 
1,2
"""




















from collections import defaultdict


class ShoppingCart(object):
	def __init__(self, combos):
		self._combos = defaultdict(list)
		for c_p in xrange(len(combos)):
			for item in combos[c_p][1]:
				self._combos[item].append((c_p+1, combos[c_p][0]))


	def _get_total_cost(self, items, pos):
		cost = 0
		used_pos = set()
		for i in xrange(len(items)):
			combo = self._combos[items[i]][pos[i]]
			if combo[0] not in used_pos:
				used_pos.add(combo[0])
				cost += combo[1]


		return cost


	def _find_min_cost_pos(self, items, options_pos, min_cost, min_cost_pos):
		print items, options_pos
		for i in xrange(len(options_pos)):
			options_pos_aux = options_pos[:]
			options_pos_aux[i] += 1
			if options_pos_aux[i] < len(self._combos[items[i]]):
				tc = self._get_total_cost(items, options_pos_aux)
				print tc, min_cost, min_cost_pos
				if tc < min_cost[0]:
					min_cost[0] = tc
					for i in xrange(len(options_pos_aux)):
						min_cost_pos[i] = options_pos_aux[i]
				self._find_min_cost_pos(
items, options_pos_aux, min_cost, min_cost_pos)


		return tuple(set([self._combos[items[i]][min_cost_pos[i]][0]
 for i in xrange(len(min_cost_pos))]))


	def get_items_to_buy(self, items):
		options_pos = [0]*len(items)
		min_cost = [self._get_total_cost(items, options_pos)]
		print "Min cost:", min_cost


		return self._find_min_cost_pos(
items, options_pos, min_cost, [0]*len(items))
	


import unittest


class TestShoppingCart(unittest.TestCase):
	def test_get_items_to_buy(self):
		sc = ShoppingCart((
			(5, ('Burger',)),
			(4, ('French_Frice',)),
			(8, ('Coldrink',)),
			(12, ('Burger', 'French_Frice', 'Coldrink',)),
			(14, ('Burger', 'Coldrink',)),


))
		self.assertEqual(sc.get_items_to_buy(('Coldrink',)), (3, ))
		self.assertEqual(sc.get_items_to_buy(('Burger', 'Coldrink',)), (4, ))
		self.assertEqual(sc.get_items_to_buy(('Burger', 'French_Frice',)), (1, 2, ))


if __name__ == '__main__':
	unittest.main()
