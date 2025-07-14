class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Recursive Solution 

        @cache
        def helper(idx):
            if idx >= n:
                return 0
            

            rob = nums[idx] + helper(idx + 2)
            skip = helper(idx+1)
        
            return max(rob, skip)
        
        return helper(0)

        # Bottom Up DP (Tabulation)

        # dp = [0] * (n+1)

        # Base Case
        # dp[1] = nums[0]

        # Space Optimization
        prev1, prev2 = 0, nums[0]


        for i in range(2, n+1):
            # dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            cur = max(prev2, prev1 + nums[i-1])
            prev1, prev2 = prev2, cur

        
        return prev2
        # return dp[n]