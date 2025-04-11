class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # count = 0

        # for num in range(low, high + 1):
        #     digits = list(map(int, str(num)))
        #     if len(digits) & 1:
        #         continue

        #     half = len(digits) >> 1
        #     if sum(digits[:half]) == sum(digits[half:]):
        #         count += 1
        
        # return count

        

        # ** DIGIT DP SOLUTION FOR LARGER CONSTRAINTS ** #

        return self._countUpTo(high) - self._countUpTo(low - 1)
    
    def _countUpTo(self, X: int) -> int:
        S = str(X)
        L = len(S)

        res = 0
        for l in range(2, L, 2):
            res += self._countForLength(l, None)
        

        if not (L & 1):
            digits = list(map(int, S))
            res += self._countForLength(L, digits)
        
        return res
    
    def _countForLength(self, L, boundDigits: Optional[List[int]]) -> int:

        half = L >> 1

        @cache
        def dp(pos: int, tight: bool, s1: int, s2: int) -> int:
            if pos == L:
                return 1 if s1 == s2 else 0
            
            low_d = 0 if pos > 0 else 1
            high_d = 9

            if tight:
                high_d = boundDigits[pos]
            
            total = 0
            for digit in range(low_d, high_d + 1):
                new_tight = tight and (digit == high_d)
                new_s1 = s1 + digit if pos < half else s1
                new_s2 = s2 if pos < half else s2 + digit
                total += dp(pos + 1, new_tight, new_s1, new_s2)
            
            return total
        

        return dp(0, True if boundDigits is not None else False, 0, 0)