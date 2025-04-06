class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # ** Approach One: Brute Force (generating all subsets and performing the constraint check) ** #
        # TC : O(2^n * n^2), SC: O(n) gives TLE

        # best_subset = []
        # def isValid(arr):
        #     for i in range(len(arr)):
        #         for j in range(i+1, len(arr)):
        #             if arr[j] % arr[i] !=0 and arr[i] % arr[j] != 0:
        #                 return False
            
        #     return True
        # for mask in range(1, 1 << n):
        #     subset = []
        #     for i in range(n):
        #         if mask & (1 << i):
        #             subset.append(nums[i])
            
        #     if isValid(subset) and len(subset) > len(best_subset):
        #         best_subset = subset
        
        # return best_subset


        # ** Approach Two: DP (based on the observation that sorting the nums array benefits to code up with optimal solution) **
        # TC: O(n^2), SC: O(n)

        nums.sort()

        dp = [1] * n # dp[i] represents the largest subset ending at i
        prev = [-1] * n # prev[i] represents predecessors of i (the largest subset ending at i)
        maxi = 0 # the maximum index until which we can get the largest subset

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > dp[maxi]:
                maxi = i
        
        res = []
        while maxi != -1:
            res.append(nums[maxi])
            # if prev[maxi] == -1:
            #     break
            maxi = prev[maxi]
        
        res.reverse()
        return res