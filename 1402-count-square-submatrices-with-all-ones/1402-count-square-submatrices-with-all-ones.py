class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        res = 0

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            dp[i][0] = matrix[i][0]
            res += dp[i][0]
        
        for j in range(1, m):
            dp[0][j] = matrix[0][j]
            res += dp[0][j]
        

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
                
                res += dp[i][j]
        
        return res