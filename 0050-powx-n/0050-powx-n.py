class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if not x:
            return 0
        res = 1
        sign = -1 if n < 0 else 1
        n = abs(n)
        while n > 1:
            if n & 1:
                res *= x
                n -= 1
            else:
                x *= x
                n //= 2
        return 1 / (res * x) if sign == -1 else res * x