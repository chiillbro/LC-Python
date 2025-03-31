class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Try picking up any two colors and color up all the nodes of the graph with alteranting colors for each edge, by the end if no two adjacent nodes are colored same (i.e., evey edge has perfect alterante colors), then that graph is said to be a Bipartite Graph..

        That's what the following bfs does.
        """
        V = len(graph)
        color = [-1] * V

        for i in range(V):
            if color[i] != -1:
                continue
            queue = deque([i])
            color[i] = 0

            while queue:
                cur = queue.popleft()
                for neigh in graph[cur]:
                    if color[neigh] == -1:
                        color[neigh] = 1 - color[cur]
                        queue.append(neigh)
                    elif color[neigh] == color[cur]:
                        return False
        
        return True
        
        
