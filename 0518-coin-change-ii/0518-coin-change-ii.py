class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Recusion + Memoization
        
        # @cache
        # def helper(idx, cur_amount):
        #     if cur_amount == 0:
        #         return 1
            
        #     if idx == len(coins) or cur_amount < 0:
        #         return 0
            
        #     use_it = helper(idx, cur_amount - coins[idx])
        #     skip = helper(idx + 1, cur_amount)

        #     return use_it + skip

        # return helper(0, amount)
        
        # Bottom Up DP
        dp = [0] * (amount + 1)

        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i-coin]
        
        return dp[amount]