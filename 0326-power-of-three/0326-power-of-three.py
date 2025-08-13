class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        if n <= 2:
            return False
        
        while n > 3:
            n /= 3
        
        return n == 3