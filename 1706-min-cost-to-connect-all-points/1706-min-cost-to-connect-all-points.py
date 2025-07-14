class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

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