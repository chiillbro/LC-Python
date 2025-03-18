class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == divisor: return 1
        res = 0
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        n, x = abs(dividend), abs(divisor)

        while x <= n:
            cnt = 0

            while n >= (x << (cnt + 1)):
                cnt += 1
            res += (1 << cnt)

            n -= (x << cnt)
        
        threshold = pow(2, 31) - 1
        
        if res > threshold:
            return threshold if sign == 1 else sign * (threshold + 1)
        
        return sign * res

