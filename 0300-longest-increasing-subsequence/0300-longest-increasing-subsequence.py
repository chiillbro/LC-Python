class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Plain DP Approach, Tabulation TC: O(N^2)
        # n = len(nums)
        # dp = [1] * n # as every element is itself a subsequence with length 1

        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)


        # Patience Sorting with Binary Search, Optimal solution for LIS problems, TC: O(N)
        LIS = []

        for num in nums:
            insert_idx = bisect_left(LIS, num)
            if insert_idx == len(LIS):
                LIS.append(num)
            else:
                LIS[insert_idx] = num
        return len(LIS)