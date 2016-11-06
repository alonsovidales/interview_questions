"""
Implement method:
    List<Range> getRanges(List<Shard> shards, List<Key> keys)
    That returns list of ranges. Each range represents multiple keys aggregated over a shard: 
    n-keys > 1-shard > l-range 

    Method should return no more than 1 range per shard that spans all keys or their parts belonging to this shard. 

    Each of the 'Range' , 'Shard' and 'Key' classes have 'end' and 'start' fields of int type, where 'start' is inclusive and 'end' is exclusive. 

Example:
    1-9, 12-59, 100-999 < shards (input)
    2-3, 6-8, 11-20, 200-220 < keys (input)
    2-8, 12-20, 200-220 < ranges (output)

Note: I decided to consider that a range of keys can be only inside a single shard
"""

class Sharding(object):
    def __init__(self, shards):
        self._shards = shards

    def _get_shard(self, key):
        print key
        for i in xrange(len(self._shards)):
            if self._shards[i][0] <= key and self._shards[i][1] > key:
                return i

    def get_ranges(self, keys):
        range_by_shard = [[float('inf'), float('-inf')] for i in xrange(len(self._shards))]

        for key in keys:
            shard = self._get_shard(key[1] - key[0] / 2)
            if range_by_shard[shard][0] > key[0]:
                if key[0] > self._shards[shard][0]:
                    range_by_shard[shard][0] = key[0]
                else:
                    range_by_shard[shard][0] = self._shards[shard][0]
            if range_by_shard[shard][1] < key[1]:
                if key[1] < self._shards[shard][1]:
                    range_by_shard[shard][1] = key[1]
                else:
                    range_by_shard[shard][1] = self._shards[shard][1]

        return range_by_shard

import unittest

class TestSharding(unittest.TestCase):
    def test_get_ranges(self):
        sharding = Sharding((
            (1,9),
            (12, 59),
            (100, 999)
        ))
        self.assertEqual(sharding.get_ranges((
            (2, 3),
            (6, 8),
            (11, 20),
            (200, 220)
        )), [
            [2, 8],
            [12, 20],
            [200, 220]
        ])

if __name__ == '__main__':
    unittest.main()
