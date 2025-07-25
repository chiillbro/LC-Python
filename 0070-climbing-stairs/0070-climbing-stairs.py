class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2

        first, second = 1, 2
        
        for i in range(3, n+1):
            # dp[i] = dp[i-1] + dp[i-2]
            cur = first + second
            second, first = cur, second

        
        # return dp[n]
        return second