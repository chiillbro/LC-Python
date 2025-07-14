class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # Floyd's Warshall Algorithm, TC: (O(V^3)), SC: O(V^2)

        # dist = [[math.inf] * n for _ in range(n)]

        # for u, v, w in edges:
        #     dist[u][v] = w
        #     dist[v][u] = w
        

        # for i in range(n):
        #     dist[i][i] = 0
        

        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # cityNumber = 0
        # cityCount = n
        # for i in range(n):
        #     cnt = 0
        #     for j in range(n):
        #         if dist[i][j] <= distanceThreshold:
        #             cnt += 1
            
        #     if cnt <= cityCount:
        #         cityCount = cnt
        #         cityNumber = i
        
        # return cityNumber


        # Using Dijkstra's Algorithm

        cnts = [0] * n

        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        
        for cur in range(n):
            dist = [math.inf] * n

            dist[cur] = 0

            pq = [(0, cur)]

            while pq:
                cur_dist, cur_node = heappop(pq)

                if cur_dist >= distanceThreshold:
                    continue
                
                for neigh, neigh_wei in adj_list[cur_node]:
                    new_dist = cur_dist + neigh_wei

                    if new_dist < dist[neigh]:
                        dist[neigh] = new_dist
                        heappush(pq, (new_dist, neigh))
            
            cnt = sum(1 for d in dist if d <= distanceThreshold)
            cnts[cur] = cnt
        

        min_cities = n
        city_number = 0

        for city, cnt in enumerate(cnts):
            if cnt <= min_cities:
                min_cities = cnt
                city_number = city
        
        return city_number


