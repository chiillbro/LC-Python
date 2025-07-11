class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        n = len(events)
        starts = [start for start, _, _ in events]
        nxt = [0] * n

        for i in range(n):
            end_time = events[i][1]

            nxt[i] = bisect_right(starts, end_time)
        

        # def findNextIndex(end_time):
        #     i, j = 0, len(events) - 1

        #     while i <= j:
        #         mid = (i + j) >> 1

        #         if events[mid][0] <= end_time:
        #             i = mid + 1
        #         else:
        #             j = mid - 1
            
        #     return i

        # memo = {}
        # def dfs(cur_idx, count):
        #     if count >= k:
        #         return 0
            
        #     if cur_idx >= len(events):
        #         return 0

        #     key = (cur_idx, count)

        #     if key in memo:
        #         return memo[key]
            
        #     cur_event_val = events[cur_idx][2]

        #     cur_end_time = events[cur_idx][1]

        #     # nxt_idx = findNextIndex(cur_end_time)

        #     take = cur_event_val + dfs(nxt[cur_idx], count + 1)

        #     skip = dfs(cur_idx + 1, count)


        #     memo[key] = max(take, skip)

        #     return memo[key]

        # dp = [[0] * (n + 1) for _ in range(k+1)]

        # for i in range(n-1, -1, -1):
        #     for j in range(1, k + 1):
        #         next_idx = findNextIndex(events[i][1])

        #         dp[j][i] = max(dp[j][i+1], events[i][2] + dp[j-1][next_idx])
                
        # return dp[k][0]
        
        # return dfs(0, 0)

        dp = [[0] * (k + 1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            cur_end, cur_val = events[i][1], events[i][2]
            for j in range(1, k + 1):
                take = cur_val + dp[nxt[i]][j-1]

                skip = dp[i+1][j]
                
                dp[i][j] = max(take, skip)
        
        return dp[0][k]