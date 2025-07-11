class Solution:
    def maxTaxiEarnings(self, k: int, rides: List[List[int]]) -> int:
        rides.sort()

        n = len(rides)

        starts = [start for start, _, _ in rides]

        nxt = [0] * n

        for i in range(n):
            cur_end = rides[i][1]

            nxt[i] = bisect_left(starts, cur_end)
        
        # memo = {}
        # def dfs(cur_idx):
        #     if cur_idx >= n:
        #         return 0
            
        #     if rides[cur_idx][1] > k:
        #         return 0
            
        #     if cur_idx in memo:
        #         return memo[cur_idx]
            
        #     cur_earn = rides[cur_idx][1] - rides[cur_idx][0] + rides[cur_idx][2]

        #     nxt_idx = nxt[cur_idx]

        #     pick = cur_earn + dfs(nxt_idx)

        #     skip = dfs(cur_idx + 1)

        #     memo[cur_idx] = max(pick, skip)

        #     return memo[cur_idx]

        # return dfs(0)

        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
                cur_earn = rides[i][1] - rides[i][0] + rides[i][2]

                nxt_idx = nxt[i]
    
                pick = cur_earn + dp[nxt_idx]
    
                skip = dp[i + 1]

                dp[i] = max(pick, skip)
        
        return dp[0]
