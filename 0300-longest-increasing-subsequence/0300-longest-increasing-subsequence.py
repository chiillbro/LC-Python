class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP Approach
        n = len(nums)
        dp = [1] * n # as every element is itself a subsequence with length 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)