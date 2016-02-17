class Solution(object):
    def _getDeep(self, graph, node, current_deep=0, max_deep=None, visited_nodes=None):
        print node, current_deep, max_deep
        if max_deep is None:
            max_deep = [0]
            visited_nodes = set([node])
            
        if current_deep > max_deep[0]:
            max_deep[0] = current_deep
            
        for child in graph[node]:
            if child not in visited_nodes:
                visited_nodes.add(child)
                self._getDeep(graph, child, current_deep+1, max_deep, visited_nodes)
          
        return max_deep[0]
        
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        print "Graph:", graph
        
        min_deep = float('+Inf')
        deeps = collections.defaultdict(list)
        for node in graph:
            deep = self._getDeep(graph, node)
            if deep <= min_deep:
                min_deep = deep
                deeps[deep].append(node)
            
        return deeps.get(min_deep, None)
