class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        low = low.zfill(n)

        pre_len = n - len(s)

        @cache
        def dfs(i, is_low, is_high):
            if i == n:
                return 1
            
            lo = int(low[i]) if is_low else 0
            hi = int(high[i]) if is_high else 9

            res = 0
            if i < pre_len:
                for digit in range(lo, min(hi, limit) + 1):
                    res += dfs(
                        i + 1,
                        is_low and digit == lo,
                        is_high and digit == hi
                    )
            else:
                x = int(s[i - pre_len])
                if lo <= x <= min(hi, limit):
                    res = dfs(
                        i + 1,
                        is_low and x == lo,
                        is_high and x == hi
                    )
            return res
        
        return dfs(0, True, True)

        
        