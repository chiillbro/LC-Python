class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return False
        
        if self.size[xRoot] < self.size[yRoot]:
            xRoot, yRoot = yRoot, xRoot
        
        self.parent[yRoot] = xRoot
        self.size[xRoot] += self.size[yRoot]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Prim's Algorithm

        in_mst = [0] * n
        total_cost = 0
        min_dist = [math.inf] * n
        min_dist[0] = 0


        for _ in range(n):
            u = -1
            for i in range(n):
                if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            
            in_mst[u] = 1
            total_cost += min_dist[u]

            x1, y1 = points[u]
            for v in range(n):
                if not in_mst[v]:
                    x2, y2 = points[v]
                    cost = abs(x1 - x2) + abs(y1 - y2)

                    if cost < min_dist[v]:
                        min_dist[v] = cost
            
        return total_cost


        # Kruskal's Algorithm
        # edges = []
        # for u in range(n):
        #     for v in range(u+1, n):
        #         cost = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
        #         edges.append((cost, u, v))
        
        # edges.sort()

        # uf = DSU(n)

        # total_cost = 0
        # for cost, u, v in edges:
        #     if uf.union(u, v):
        #         total_cost += cost

        # return total_cost
        
