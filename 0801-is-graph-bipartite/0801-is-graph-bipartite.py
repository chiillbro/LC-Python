class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
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
        
        
