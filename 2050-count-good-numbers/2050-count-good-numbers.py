class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10, 9) + 7

        # for even indices, there are 5 choices (0, 2, 4, 6, 8)
        # for odd indices, there are 4 choices (2, 3, 5, ,7)

        # 2. total good numbers -> 
        # if n is even, the total no.of good numbers is 5^(n/2) * 4 ^(n/2) = 20 ^ (n/2)
        # if n is odd, the total no.of good numbers is 5 * 20^((n-1)/2)

        def expo(x: int, n : int) -> int:
            """
            returns the x ** n value
            """
            if not n:
                return 1
            
            if n & 1:
                return x * expo(x, n - 1) % MOD
            
            return expo(x * x % MOD, n >> 1) 
        
        return 5 ** (n%2) * expo(20, n // 2) %MOD


        