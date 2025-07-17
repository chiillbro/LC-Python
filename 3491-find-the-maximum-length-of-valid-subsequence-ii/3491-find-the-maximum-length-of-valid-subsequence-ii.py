class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        # for a k, we would have 0...k-1 remainders

        # let's suppose, two elements in a subsequence form a sum = C, i.e., 

            # r1 = sub[i] % k, r2 = sub[i+1] % k
            # (r1 + r2) % k = C

            # so the currnet longest subsequence can be formed r1, r2, r1, r2, r1...r2
        
        # so, the remainder that we get at every number in nums, we need to find it's remainder pair that sums up to this target sum (C) and the remainder pair can be in the range of 0...k-1

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