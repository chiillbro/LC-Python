class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adj_list = {i : [] for i in range(n)}

        # for u, v, price in flights:
        #     adj_list[u].append((v, price))
        
        # # prices = [float("inf")] * n
        # # prices[src] = 0
        # prices = [[float("inf")] * (k + 2) for _ in range(n)]
        # prices[src][0] = 0
        # heap = [(0, src, 0)]

        # while heap:
        #     cur_price, cur_node, stops = heappop(heap)
            
        #     if cur_node == dst:
        #         return cur_price

        #     if stops == k + 1: continue

        #     for neigh, price in adj_list[cur_node]:
        #         next_cost = cur_price + price
        #         next_stops = stops + 1
        #         if next_cost < prices[neigh][next_stops]:
        #             prices[neigh][next_stops] = next_cost
        #             heappush(heap, (next_cost, neigh, next_stops))

        # return -1

        # ** Approach 2: Using Modified Dijkstra with Queue ** #

        # prices = [float("inf")] * n
        # queue = deque([(0, src, 0)])
        # prices[src] = 0

        # while queue:
        #     cur_stops, cur_node, cur_cost = queue.popleft()

        #     if cur_stops == k + 1: continue

        #     for neigh, price in adj_list[cur_node]:
        #         next_cost = cur_cost + price
        #         next_stops = cur_stops + 1
        #         if next_cost < prices[neigh] and next_stops <= k + 1:
        #             prices[neigh] = next_cost
        #             queue.append((next_stops, neigh, next_cost))
        

        # return -1 if prices[dst] == float("inf") else prices[dst]

        # ** Approach 3: using modified Bellman Ford algorithm ** #

        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()
            for u, v, price in flights:
                if prices[u] == float("inf"):
                    continue
                
                if prices[u] + price < temp[v]:
                    temp[v] = prices[u] + price
            
            prices = temp
        
        return -1 if prices[dst] == float('inf') else prices[dst]