class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        n = len(nums)

        # dp = [0] * (n+1)

        # dp[1] = nums[0]

        # Space Optimize
        prev2, prev1 = 0, nums[0]

        for i in range(2, n + 1):
            # dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            cur = max(prev1, prev2 + nums[i-1])
            prev2, prev1 = prev1, cur
        
        return prev1