class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        
        # dp[i] represents no.of ways to decode the prefix string s[0:i-1] inclusively
        dp = [0] * (n + 1)

        # empty string can be decoded in 1 way which is to do nothing
        dp[0] = 1
        
        # 1 length valid string if it is not "0", then there is one way to decode it "1" to "9"        
        dp[1] = 1

        for i in range(2, n+1):
            # if the current char is not "0", then we can extend all the ways of dp[i-1] to a new way
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            
            # if the cur and last chars number is a valid two digit chunk, then it again can extend the ways of dp[i-2] to a new way
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]