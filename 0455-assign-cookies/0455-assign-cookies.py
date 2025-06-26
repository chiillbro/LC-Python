class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            
            j += 1
        
        return i


        # DP, for learning, memory limit exceeded, O(n * m) for both complexities

        # n, m = len(g), len(s)
        # dp = [[0] * (m+1) for _ in range(n+1)]


        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if g[i-1] <= s[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = dp[i-1][j]
        
        # return dp[-1][-1]