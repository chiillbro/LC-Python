class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {i : [] for i in range(n)}

        for u, v, price in flights:
            adj_list[u].append((v, price))
        
        # prices = [float("inf")] * n
        # prices[src] = 0
        prices = [[float("inf")] * (k + 2) for _ in range(n)]
        prices[src][0] = 0
        heap = [(0, src, 0)]

        while heap:
            cur_price, cur_node, stops = heappop(heap)
            
            if cur_node == dst:
                return cur_price

            if stops == k + 1: continue

            for neigh, price in adj_list[cur_node]:
                next_cost = cur_price + price
                next_stop = stops + 1
                if next_cost < prices[neigh][next_stop]:
                    prices[neigh][next_stop] = next_cost
                    heappush(heap, (next_cost, neigh, next_stop))

        return -1