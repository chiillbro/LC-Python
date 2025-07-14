class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Recursion

        @cache
        def helper(cur_amount):
            if cur_amount == 0:
                return 0
            
            if cur_amount < 0:
                return math.inf

            best = math.inf
            for coin in coins:
                next_coins = helper(cur_amount - coin)

                if next_coins != math.inf:
                    best = min(best, next_coins + 1)
            
            return best
        
        res = helper(amount)

        return res if res != math.inf else -1
