# Still some cases to fix
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]
        edges = []
        for building in buildings:
            edges.append((building[0], building[2], True))
            edges.append((building[1], building[2], False))
            
        # edges == [(2, 10, True), (3, 15, True), (9, 10, False), (7, 15, False), ...]
        edges = sorted(edges, key=lambda x: (x[0], not x[2]))
        print edges
        result = []
        current_height = 0
        active_heights = collections.defaultdict(int)
        for edge in edges:
            if edge[2] and edge[1] > current_height:
                current_height = edge[1]
                if len(result) > 0 and result[len(result)-1][0] == edge[0]:
                    if result[len(result)-1][0] < current_height:
                        print "Replacing:", edge[0], current_height
                        result[len(result)-1][1] = current_height
                else:
                    print "Appending:", edge[0], current_height
                    result.append([edge[0], current_height])
                    
                active_heights[edge[1]] += 1
            elif not edge[2]:
                active_heights[edge[1]] -= 1
                if active_heights[edge[1]] == 0:
                    del active_heights[edge[1]]
                    
                    if len(active_heights) == 0:
                        result.append([edge[0], 0])
                        current_height = 0
                    elif edge[1] != current_height:
                        prev_height = current_height
                        current_height = 0
                        for height in active_heights.keys():
                            if current_height < height:
                                current_height = height
                        print prev_height, current_height
                        if prev_height != current_height:
                            result.append([edge[0], current_height])
        
        if len(edges) and current_height != 0:
            result.append((edges[len(edges)-1][0], 0))
        
        return result
