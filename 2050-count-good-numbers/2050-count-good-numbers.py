class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        # Efficient exponentiation - Exponentiation by Squaring or Binary Exponentiation
        def expo(x, n):
            """
            Calculates x**n in an efficient way
            """
            if not n:
                return 1
            
            if n & 1:
                return x * expo(x, n - 1) % MOD
            
            return expo((x*x) % MOD, n >> 1)


        # if n is even: there are 5 choices - (0. 2, 4, 6, 8)
        # if n is odd: there are 4 choices - (2, 3, 5, 7)

        # so, if n == 1: which is odd, good numbers = 5^1 * 4^0 = 5
        # if n == 2: which is even, good numbers = 5^1 * 4^1 = 20
        # if n == 3: which is odd, good numbers = 5^2 * 4^1 = 100
        # if n == 4: which is even, good numbers = 5^2 & 4^2 = 400

        # Number of even spots = (n + 1) // 2 (integer division, rounds down for n/2 if n is even, and is correct for odd n) or more simply, ceil(n/2)
        # Number of odd spots = n // 2 (integer division)


        # so (even, odd) pairs are n // 2 it can be simplified to (5 * 4) ^ (n//2)
        # and the remaining 1 spot if n is odd else 0 -> n%2, these spot has 5 choices to be filled with even numbers - 5^(n%2)
        return 5 ** (n%2) * expo(20, n >> 1) % MOD