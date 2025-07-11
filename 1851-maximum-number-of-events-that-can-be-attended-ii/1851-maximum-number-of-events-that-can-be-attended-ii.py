class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()

        n = len(events)

        def findNextIndex(end_time):
            i, j = 0, len(events) - 1

            while i <= j:
                mid = (i + j) >> 1

                if events[mid][0] <= end_time:
                    i = mid + 1
                else:
                    j = mid - 1
            
            return i

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

        #     nxt_idx = findNextIndex(cur_end_time)

        #     cur_event_val += dfs(nxt_idx, count + 1)

        #     skip = dfs(cur_idx + 1, count)


        #     memo[key] = max(cur_event_val, skip)

        #     return memo[key]

        dp = [[0] * (n + 1) for _ in range(k+1)]

        for i in range(n-1, -1, -1):
            for j in range(1, k + 1):
                next_idx = findNextIndex(events[i][1])

                dp[j][i] = max(dp[j][i+1], events[i][2] + dp[j-1][next_idx])
                
        return dp[k][0]
        
        # return dfs(0, 0)

        # dp = [[0] * (len(events) + 1) for _ in range(k+1)]
        # end_date = 0
        # for i in range(1, k+1):
        #     for j in range(1, len(events) + 1):
        #         if events[j-1][0] > end_date:
        #             dp[i][j] = max(dp[i-1]) + events[j-1][2]
        #             end_date = events[j-1][1]
        #         else:
        #             dp[i][j] = max(dp[i-1])
        
        # return max(dp[k])