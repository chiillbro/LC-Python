class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        n = len(events)

        # starts = [start for start, _, _ in events]

        # nxt = [0] * n

        # for i in range(n):
        #     nxt[i] = bisect_right(starts, events[i][1])
        
        # dp = [[0] * 3 for _ in range(n + 1)]

        # for i in range(n-1, -1, -1):
        #     cur_val = events[i][2]

        #     for j in range(1, 3):
        #         attend = cur_val + dp[nxt[i]][j-1]

        #         skip = dp[i + 1][j]

        #         dp[i][j] = max(attend, skip)
        
        # return dp[0][2]


        # Priority Queue Approach

        pq = []
        ans = 0
        max_value = 0
        for event in events:
            while pq and pq[0][0] < event[0]:
                max_value = max(pq[0][1], max_value)
                heappop(pq)
            
            ans = max(ans, max_value + event[2])

            heappush(pq, (event[1], event[2]))
        
        return ans