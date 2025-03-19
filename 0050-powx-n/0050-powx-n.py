class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if not x:
            return 0
        # extra = 1
        # sign = 0 if n < 0 else 1
        # n = abs(n)
        # while n > 0:
        #     if n & 1:
        #         extra *= x
        #         n -= 1
        #     else:
        #         x *= x
        #         n >>= 1
        # return 1 / extra if not sign else extra


        def calculate(x, n):
            if n == 0:
                return 1
            elif n & 1:
                return x * calculate(x, n - 1)
            
            return calculate(x * x, n >> 1)

        return 1/calculate(x, abs(n)) if n < 0 else calculate(x, abs(n))