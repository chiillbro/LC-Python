class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)

        for u, v, t in times:
            adj_list[u].append((v, t))

        dist = [math.inf] * (n+1)

        dist[k] = 0

        pq = [(0, k)]

        while pq:
            cur_time, cur_node = heappop(pq)

            for nei_node, nei_time in adj_list[cur_node]:
                new_time = cur_time + nei_time

                if new_time < dist[nei_node]:
                    dist[nei_node] = new_time
                    heappush(pq, (new_time, nei_node))

        max_time = 0
        for time in dist[1:]:
            if time == math.inf:
                return -1
            
            max_time = max(time, max_time)
        
        return max_time