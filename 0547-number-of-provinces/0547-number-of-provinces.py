class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connected_components = 0
        visited = set()

        n = len(isConnected)

        def dfs(node):
            visited.add(node)

            for i in range(n):
                if isConnected[node][i] and i not in visited:
                    dfs(i)
        
        for i in range(n):
            if i not in visited:
                connected_components += 1
                dfs(i)
        
        return connected_components