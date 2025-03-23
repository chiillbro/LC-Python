class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        res = 0

        graph = [[] for _ in range(n)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        shortest_time = [float('inf')] * n 
        shortest_time[0] = 0
        path_count = [0] * n
        path_count[0] = 1

        min_heap = [(0, 0)]

        while min_heap:
            cur_time, cur_node = heappop(min_heap)

            if cur_time > shortest_time[cur_node]: continue

            for neigh_node, road_time in graph[cur_node]:
                if cur_time + road_time < shortest_time[neigh_node]:
                    shortest_time[neigh_node] = cur_time + road_time
                    path_count[neigh_node] = path_count[cur_node]
                    heappush(min_heap, (shortest_time[neigh_node], neigh_node))
                
                elif cur_time + road_time == shortest_time[neigh_node]:
                    path_count[neigh_node] = (
                        path_count[neigh_node] + path_count[cur_node]
                    ) % MOD
        
        return path_count[n-1]