from typing import List
import math
from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Convert bounds to strings of equal length.
        low = str(start)
        high = str(finish)
        n = len(high)
        low = low.zfill(n)  # Ensure low has length n
        
        # Calculate the length of the prefix (free digits) before the forced suffix.
        pre_len = n - len(s)

        @cache
        def dfs(i: int, is_low: bool, is_high: bool) -> int:
            # If we have processed all positions, this yields 1 valid number.
            if i == n:
                return 1
            
            # Determine digit boundaries for the current position.
            # If we are tight to the lower bound, lo = digit from low; otherwise, 0.
            lo = int(low[i]) if is_low else 0
            # If we are tight to the upper bound, hi = digit from high; otherwise, 9.
            hi = int(high[i]) if is_high else 9
            
            res = 0
            # For positions in the prefix where we have a free choice.
            if i < pre_len:
                for digit in range(lo, min(hi, limit) + 1):
                    res += dfs(
                        i + 1,
                        is_low and (digit == lo),
                        is_high and (digit == hi)
                    )
            else:
                # For the forced suffix, the digit must equal the corresponding digit of s.
                required_digit = int(s[i - pre_len])
                # If the forced digit is within bounds and within the limit.
                if lo <= required_digit <= min(hi, limit):
                    res = dfs(
                        i + 1,
                        is_low and (required_digit == lo),
                        is_high and (required_digit == hi)
                    )
            return res
        
        return dfs(0, True, True)