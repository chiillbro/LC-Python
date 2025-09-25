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

        dp = []

        for i in range(n):
            j = len(triangle[i])

            dp.append([0] * j)
        
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(len(triangle[i])):
                prev1 = dp[i-1][j] if j < len(triangle[i-1]) else inf
                prev2 = dp[i-1][j-1] if j-1 >= 0 else inf

                dp[i][j] = triangle[i][j] + min(prev1, prev2)
        

        return min(dp[-1])

