class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Recursion

        # @cache
        # def helper(cur_amount):
        #     if cur_amount == 0:
        #         return 0
            
        #     if cur_amount < 0:
        #         return math.inf

        #     best = math.inf
        #     for coin in coins:
        #         next_coins = helper(cur_amount - coin)

        #         if next_coins != math.inf:
        #             best = min(best, next_coins + 1)
            
        #     return best
        
        # res = helper(amount)

        # return res if res != math.inf else -1


        # Bottom Up DP

        dp = [math.inf] * (amount + 1)

        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:
                if x - coin >= 0:
                    dp[x] = min(dp[x], dp[x-coin] + 1)
        
        return dp[amount] if dp[amount] != math.inf else -1

        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] = min(dp[i], dp[i-coin] + 1)
        
        # return dp[amount] if dp[amount] != amount + 1 else -1
