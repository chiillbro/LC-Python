class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected_components = 0
        visited = set()
        n = len(isConnected)

        # ** DFS Approach ** #
        # def dfs(node):
        #     visited.add(node)

        #     for i in range(n):
        #         if isConnected[node][i] and i not in visited:
        #             dfs(i)
        
        # for i in range(n):
        #     if i not in visited:
        #         connected_components += 1
        #         dfs(i)

        # ** BFS Approach ** #

        def bfs(node):
            queue = deque([node])
            visited.add(node)

            while queue:
                node = queue.popleft()
                for i in range(n):
                    if isConnected[node][i] and i not in visited:
                        queue.append(i)
                        visited.add(i)
        
        for i in range(n):
            if i not in visited:
                connected_components += 1
                bfs(i)

                    
        return connected_components