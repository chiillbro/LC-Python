class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        dp = [1] * n
        prev = [-1] * n
        maxi = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 >= dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            maxi = i if dp[i] > dp[maxi] else maxi
        
        res = []
        while maxi != -1:
            res.append(nums[maxi])
            maxi = prev[maxi]
        
        return res[::-1]