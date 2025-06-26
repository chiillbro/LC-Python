class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # if m > n:
        #     n, m = m, n
        
        # dp = [[0] * (m + 1) for _ in range(n+1)]

        # space optimization

        prev = [0] * (m+1)

        for i in range(1, n+1):
            cur = [0] * (m+1)
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    # dp[i][j] = dp[i-1][j-1] + 1
                    cur[j] = prev[j-1] + 1
                else:
                    # dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    cur[j] = max(prev[j], cur[j-1])
            
            prev = cur
        
        return prev[-1]
