class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        1. Try picking up any two colors and color up all the nodes of the graph with alteranting colors for each edge, by the end if no two adjacent nodes are colored same (i.e., evey edge has perfect alterante colors), then that graph is said to be a Bipartite Graph..

        2. One more property of Bipartite graph is, if there is a cycle exists in the graph and the path length of that cycle is odd length, then that graph can never be a Bipartite.

        That's what the following bfs does.
        """
        V = len(graph)
        color = [-1] * V

        # for i in range(V):
        #     if color[i] != -1:
        #         continue
        #     queue = deque([i])
        #     color[i] = 0

        #     while queue:
        #         cur = queue.popleft()
        #         for neigh in graph[cur]:
        #             if color[neigh] == -1:
        #                 color[neigh] = 1 - color[cur]
        #                 queue.append(neigh)
        #             elif color[neigh] == color[cur]:
        #                 return False
        
        # return True


        # ** DFS Appraoch

        def dfs(node, col):
            color[node] = col
            for neigh in graph[node]:
                if color[neigh] == -1:
                    if not dfs(neigh, 1 - col):
                        return False
                elif color[neigh] == col:
                    return False
            return True
        
        for i in range(V):
            if color[i] != -1:
                continue
            if not dfs(i, 0):
                return False
        
        return True

        
        
