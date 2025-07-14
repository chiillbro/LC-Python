class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[math.inf] * n for _ in range(n)]

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        

        for i in range(n):
            dist[i][i] = 0
        

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        cityNumber = 0
        cityCount = n
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt += 1
            
            if cnt <= cityCount:
                cityCount = cnt
                cityNumber = i
        
        return cityNumber