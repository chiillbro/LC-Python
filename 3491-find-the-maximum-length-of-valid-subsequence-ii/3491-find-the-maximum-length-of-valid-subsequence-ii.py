class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        dp = [[0] * k for _ in range(k)]

        for num in nums:
            r2 = num % k
            for r1 in range(k):
                dp[r1][r2] = dp[r2][r1] + 1
            
        max_val = 0

        for r1 in range(k):
            for r2 in range(k):
                max_val = max(dp[r1][r2], max_val)
        
        return max_val