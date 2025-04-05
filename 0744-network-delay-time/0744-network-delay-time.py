class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # ** Approach one: using Dijkstra's Algorithm, since weights are positive ** #
        # ** TC: O(E log V), SC: O()

        adj_list = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        delays = [float("inf")] * (n+1)
        delays[k] = 0

        heap = [(0, k)]

        while heap:
            cur_delay, cur_node = heappop(heap)

            for neigh, time in adj_list[cur_node]:
                if cur_delay + time < delays[neigh]:
                    delays[neigh] = cur_delay + time
                    heappush(heap, (cur_delay + time, neigh))
        
        ans = max(delays[1:])
        return ans if ans != float('inf') else -1


        # ** Approach 2: Using Bellman Ford - but unnecessary extra complexity, which runs in O(V * E), useful for negative weights and detecting negative cycles **

        # delays = [float('inf')] * (n + 1)
        # delays[k] = 0

        # for _ in range(n):
        #     for u, v, time in times:
        #         if delays[u] == float("inf"):
        #             continue
        #         if delays[u] + time < delays[v]:
        #             delays[v] = delays[u] + time
        
        # max_time = max(delays[1:])
        # return -1 if max_time == float('inf') else max_time