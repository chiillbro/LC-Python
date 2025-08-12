class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        # dp[i][k] represents distinct integer selection sets of first i integers whose powers of x sums to k 
        dp = [[0] * (n+1) for _ in range(n+1)]

        
        dp[0][0] = 1 # 1 distinct selection to sum upto 0  which is 0^x = 0

        for i in range(1, n+1):
            cur = i**x

            for k in range(n+1):
                # skip
                dp[i][k] = dp[i-1][k]

                # take, can only happen, if the x power of current i: <= k
                if cur <= k:
                    dp[i][k] = (dp[i-1][k] + dp[i-1][k-cur]) % MOD
        
        return dp[n][n] # no.of distinct ways of selection sets with first n integers of whose x powers sums to n