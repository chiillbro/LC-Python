class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # def backtrack(row, col):
        #     if row >= n or col >= len(triangle[row]):
        #         return 0
            
        #     cur = backtrack(row+1, col)
        #     skip = backtrack(row+1, col+1)

        #     return triangle[row][col] + min(cur, skip)
        
        # return backtrack(0, 0)

        # dp = [[0] * len(row) for row in triangle]
        
        # dp[0][0] = triangle[0][0]

        prev = [triangle[0][0]]

        # Follow up

        for i in range(1, n):
            cur = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                # par1 = dp[i-1][j] if j < len(triangle[i-1]) else inf
                # par2 = dp[i-1][j-1] if j-1 >= 0 else inf

                par1 = prev[j] if j < len(triangle[i-1]) else inf
                par2 = prev[j-1] if j-1 >= 0 else inf

                # dp[i][j] = triangle[i][j] + min(par1, par2)
                cur[j] = triangle[i][j] + min(par1, par2)

            prev = cur
        

        # return min(dp[-1])
        return min(prev)

