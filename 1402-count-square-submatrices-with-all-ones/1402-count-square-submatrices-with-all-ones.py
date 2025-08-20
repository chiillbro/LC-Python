class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        res = 0

        # dp = [[0] * m for _ in range(n)]

        # for i in range(n):
        #     dp[i][0] = matrix[i][0]
        #     res += dp[i][0]
        
        # for j in range(1, m):
        #     dp[0][j] = matrix[0][j]
        #     res += dp[0][j]

        # SPACE OPTIMIZATION

        prev = 0
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i-1][j-1] == 1:
                    temp = dp[j]

                    dp[j] = 1 + min(prev, dp[j-1], dp[j])
                    prev = temp

                    res += dp[j]
                else:
                    dp[j] = 0
        

        # for i in range(1, n):
        #     for j in range(1, m):
        #         if matrix[i][j] == 1:
        #             dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
                
        #         res += dp[i][j]
        
        return res