class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for i in range(low, high + 1):
            num = str(i)
            if len(num) & 1:
                continue
            
            digits = list(map(int, num))
            half = len(digits) >> 1
            if sum(digits[:half]) == sum(digits[half:]):
                res += 1
        
        return res