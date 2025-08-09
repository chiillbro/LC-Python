class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 2:
            n /= 2
        
        if n == 2:
            return True
        
        return False