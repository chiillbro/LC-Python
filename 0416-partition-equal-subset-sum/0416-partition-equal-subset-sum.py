class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum & 1:
            return False

        
        target = _sum >> 1
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[target] == True:
                    return True
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
        
        
        