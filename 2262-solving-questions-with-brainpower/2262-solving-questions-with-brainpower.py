class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        # ** Recursive Top-Down Approach ** #
        # @lru_cache(maxsize=None)
        # def dfs(i):
        #     if i >= n: return 0

        #     pts, skip = questions[i]
        #     return max(pts+dfs(i + skip + 1), dfs(i + 1))
        
        # return dfs(0)

        # ** Optimized Bottom-Up Approach: DP ** #

        dp = [0] * n
        dp[n-1] = questions[n-1][0]

        for i in range(n-2, -1, -1):
            pts, skip = questions[i]
            dp[i] = pts

            if i + skip < n-1:
                dp[i] += dp[i+skip+1]
            
            dp[i] = max(dp[i], dp[i+1])
        
        return dp[0]