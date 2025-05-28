class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        n, m = len(edges1) + 1, len(edges2) + 1
        if not k:
            return [1] * n

        adj_list_1 = defaultdict(list)
        adj_list_2 = defaultdict(list)

        for a, b in edges1:
            adj_list_1[a].append(b)
            adj_list_1[b].append(a)
        
        for a, b in edges2:
            adj_list_2[a].append(b)
            adj_list_2[b].append(a)

        def dfs(node, parent, adj, k):
            if k < 0:
                return 0
            res = 1
            for neigh in adj[node]:
                if neigh != parent:
                    res += dfs(neigh, node, adj, k-1)
            
            return res
            
        
        max_edges = float("-inf")
        for i in range(m):
            max_edges = max(max_edges, dfs(i, -1, adj_list_2, k - 1))
        
        res = [0] * n
        for i in range(n):
            res[i] += dfs(i, -1, adj_list_1, k) + max_edges
        
        return res