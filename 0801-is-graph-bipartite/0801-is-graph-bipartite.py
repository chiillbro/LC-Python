class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        visited = [0] * n
        # colors I pick - 1 & 2
        for i in range(n):
            if visited[i]:
                continue
            queue = deque([i])
            visited[i] = 1

            while queue:
                cur = queue.popleft()

                for neigh in graph[cur]:
                    if not visited[neigh]:
                        visited[neigh] = 1 if visited[cur] == 2 else 2
                        queue.append(neigh)
                    elif visited[cur] == visited[neigh]:
                        return False

        return True