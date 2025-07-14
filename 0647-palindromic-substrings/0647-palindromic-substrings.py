class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0
        def expandAroundCenter(i, j):
            nonlocal count
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1


        for center in range(n):
            expandAroundCenter(center, center)
            expandAroundCenter(center, center + 1)
        
        return count


        # DP Approach

        # dp = [[False] * n for _ in range(n)]

        # count = 0
        # for i in range(n):
        #     dp[i][i] = True
        #     count += 1
        
        # for L in range(2, n+1):
        #     for i in range(n - L + 1):
        #         j = i + L - 1
        #         if s[i] == s[j]:
                    
        #             if L == 2 or dp[i+1][j-1]:
        #                 dp[i][j] = True
        #                 count += 1
        
        # return count