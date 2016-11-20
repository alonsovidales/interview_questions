"""
You are the main character in a game where you have to defeat a number of
enemies in order. The player has a strength value and an initial amount of
money. Each enemy also has a strength value, plus a price. 

When facing each enemy you can either: 
    1) Fight him (if your strength is enough). You keep your money. 
    2) Bribe him (if you have the necessary money). You subtract the enemy's
       price from your money, and it joins you and adds its strength to yours. 

    Given a starting strength and amount of money, calculate the optimal
    strategy and the amount of money you end with (-1 if impossible). 

    This can be easily solved recursively in O(2^n) basically trying out each
    option at every enemy. But is there a polynomial solution, maybe involving
    DP?
"""

class Game(object):
    def __init__(self, streingth, money):
        self._streingth = streingth
        self._money = money

    def play(self, enemies, streingth=None, money=None, max_money=None):
        if streingth is None:
            streingth = self._streingth
            money = self._money
            max_money = [-1]

        if streingth < 0 or money < 0:
            return max_money[0]

        if len(enemies) == 0:
            if money > max_money[0]:
                max_money[0] = money

            return max_money[0]

        self.play(enemies[1:], streingth-enemies[0][0], money, max_money)
        self.play(enemies[1:], streingth, money-enemies[0][1], max_money)

        return max_money[0]


import unittest

class TestGame(unittest.TestCase):
    def test_play(self):
        gm = Game(4, 3)
        self.assertEqual(gm.play((
            (2, 3),
            (1, 2),
            (2, 3),
        )), 1)

        self.assertEqual(gm.play(()), 3)

        self.assertEqual(gm.play((
            (2, 3),
            (2, 3),
        )), 3)

        self.assertEqual(gm.play((
            (9, 9),
            (9, 9),
        )), -1)


if __name__ == '__main__':
    unittest.main()
