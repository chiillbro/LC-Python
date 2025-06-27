class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, c in flights:
            adj_list[u].append((v, c))
        

        # dist = [math.inf] * n
        dist = [[math.inf] * (k+2) for _ in range(n)]

        queue = deque([(src, 0)])

        dist[src][0] = 0

        ans = math.inf
        while queue:
            # cur_cost, cur_stop, cur_stops = queue.popleft()
            cur_stop, cur_stops = queue.popleft()

            if cur_stops > k:
                continue
            
            for neigh, cost in adj_list[cur_stop]:
                new_cost = dist[cur_stop][cur_stops] + cost
                if new_cost < dist[neigh][cur_stops + 1]:
                    dist[neigh][cur_stops + 1] = new_cost

                    queue.append((neigh, cur_stops + 1))
                    if neigh == dst:
                        ans = min(ans, new_cost)
        
        return ans if ans != math.inf else -1



        # Dikstra's Algorithm

        # dist = [math.inf] * n

        # min_stops = [math.inf] * n

        # heap = [(0, src, 0)]
        # # dist[src] = 0

        # min_stops[src] = 0

        # while heap:
        #     best_cost, cur_stop, cur_stops = heapq.heappop(heap)

        #     if cur_stop == dst:
        #         return best_cost
            
        #     if cur_stops > k:
        #         continue
            
        #     if cur_stops > min_stops[cur_stop]: continue

        #     min_stops[cur_stop] = cur_stops
            

        #     for neigh, cost in adj_list[cur_stop]:
        #         # if best_cost + cost < dist[neigh]:
        #         heapq.heappush(heap, (best_cost + cost, neigh, cur_stops + 1))
        
        # return -1


        # Bellman Ford 

        # dist = [math.inf] * n
        # dist[src] = 0

        # for _ in range(k+1):
        #     temp = dist.copy()

        #     # for u in range(n):
        #     #     if dist[u] == math.inf: continue
        #     #     for v, w in adj_list[u]:
        #     for u, v, w in flights:
        #         temp[v] = min(temp[v], dist[u] + w)

        #     dist = temp
        

        # return dist[dst] if dist[dst] != math.inf else -1