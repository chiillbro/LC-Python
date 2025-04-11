class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            digits = list(map(int, str(num)))
            if len(digits) & 1:
                continue
                
            half = len(digits) >> 1
            if sum(digits[:half]) == sum(digits[half:]):
                count += 1
        
        return count