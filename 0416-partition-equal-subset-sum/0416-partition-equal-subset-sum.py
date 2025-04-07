class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # ** Brute Force Approach ** #
        # TC: O(2^n), SC: O(n) gives TLE
        n = len(nums)
        _sum = sum(nums)
        if _sum & 1:
            return False
        
        target = _sum >> 1

        # for mask in range(1, 1 << n):
        #     subset_sum = 0
        #     for i in range(n):
        #         if mask & (1 << i):
        #             subset_sum += nums[i]
            
        #     if subset_sum == target:
        #         return True
        
        # return False

        # ** Brute Force using Recursive Backtracking - TLE(withoug memoization) ** #
        memo = {} # added memoization
        def backtrack(i, cur_sum):
            if i == n:
                return cur_sum == 0

            if cur_sum < 0:
                return False

            if cur_sum == 0:
                return True
            
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
        
            res = backtrack(i+1, cur_sum) or backtrack(i+1, cur_sum - nums[i])
            memo[(i, cur_sum)] = res
            return res
            
        return backtrack(0, target)


        