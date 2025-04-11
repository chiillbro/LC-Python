class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            num_str = str(num)
            if len(num_str) & 1:
                continue
            
            digits = list(map(int, num_str))
            half = len(digits) >> 1
            if sum(digits[:half]) == sum(digits[half:]):
                count += 1
        
        return count