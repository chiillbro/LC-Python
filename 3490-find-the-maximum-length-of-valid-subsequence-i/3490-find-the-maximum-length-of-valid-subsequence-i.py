class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)

        # can think of dp

        # 3 conditions
            # 1. every number in the subsequence should be even
            # 2. every number in the subsequence should be odd
            # 3. alternate even, odd for every pair of numbers
        
        evens = odds = alt_end_even = alt_end_odd = 0

        for num in nums:
            if num & 1:
                odds += 1
                alt_end_odd = alt_end_even + 1
            else:
                evens += 1
                alt_end_even = alt_end_odd + 1
    
        return max(evens, odds, alt_end_even, alt_end_odd)




        # dp[i][j] represents the longest subsequence from 0...i with j parity (even, odd, even/odd)

        # dp = [[0] * 3 for _ in range(n + 1)]

        # for i in range(1, n+1):
        #     cur = nums[i-1]

        #     if cur & 1:
        #         dp[i][1] = dp[i-1][1] + 1
        #         if i == 1:
        #             dp[i][2] = 1
        #         else:
        #             dp[i][2] = 
        #         d[i][0] = dp[i-1][0]
        #     else:
        #         dp[i][0] = dp[i-1][0] + 1
        #         if i == 1:
        #             dp[i][2] = 1
        #         else:
        #             dp[i][2] =  
        #         dp[i][1] = dp[i-1][1]

        # return max(dp[-1])