class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        cnt = [0] * (n+1)

        for factor, _ in items:
            cnt[factor] += 1

        divisible_by = [0] * (n+1)

        for f in range(1, n+1):
            for multiple in range(f, n+1, f):
                divisible_by[f] += cnt[multiple]

        freecount = []
        for factor, _ in items:
            freecount.append(divisible_by[factor] - 1)
        

        minP = float("inf")
        for _, price in items:
            minP = min(price, minP)
        

        ans = 0

        items_sorted = sorted(zip(items, freecount), key=lambda x: x[0][1])
        for item, freecount_i in items_sorted:
            price_i = item[1]
            if price_i >= 2*minP:
                break

            can_buy = min(budget//price_i, freecount_i)

            budget_used = can_buy * price_i

            budget -= budget_used

            ans += can_buy * 2
        
        ans += budget // minP
        
        return ans


