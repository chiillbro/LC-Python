class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if not x:
            return 0
        extra = 1
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
            nonlocal extra
            if n == 0:
                return
            
            if n & 1:
                extra *= x
                n -= 1
            else:
                x *= x
                n >>= 1
            
            calculate(x, n)

        calculate(x, abs(n))
        return extra if n > 0 else 1 / extra