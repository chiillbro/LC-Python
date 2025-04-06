class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
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