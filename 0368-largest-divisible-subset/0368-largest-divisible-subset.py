class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        prev = [-1] * n
        maxi = 0

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
        
        return res