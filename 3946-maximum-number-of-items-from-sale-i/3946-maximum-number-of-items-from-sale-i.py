class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freecount_i = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    freecount_i[i] += 1
        

        dp = [0] * (budget + 1)

        for i in range(n):
            price_i = items[i][1]
            value_i = 1 + freecount_i[i]

            for b in range(budget, price_i - 1, -1):
                dp[b] = max(dp[b], dp[b-price_i] + value_i)
        


        minP = float("inf")

        for _, price in items:
            minP = min(minP, price)
        
        return max(dp[b] + (budget-b)//minP for b in range(budget+1))