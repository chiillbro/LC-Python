class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        n = len(nums)

        # dp = [0] * (n + 1)

        # dp[1] = nums[0]

        prev2, prev1 = 0, nums[0]

        for i in range(2, n+1):
            # dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
            cur = max(nums[i-1] + prev2, prev1)

            prev1, prev2 = cur, prev1

        # return dp[n]
        return prev1