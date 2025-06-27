class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, c in flights:
            adj_list[u].append((v, c))
        

        dist = [math.inf] * n

        queue = deque([(0, src, 0)])

        dist[src] = 0

        while queue:
            cur_cost, cur_stop, cur_stops = queue.popleft()

            if cur_stops > k:
                continue
            
            for neigh, cost in adj_list[cur_stop]:
                if cur_cost + cost < dist[neigh]:
                    dist[neigh] = cur_cost + cost

                    queue.append((cur_cost + cost, neigh, cur_stops + 1))
        
        return dist[dst] if dist[dst] != math.inf else -1
                    