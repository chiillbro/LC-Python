class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Direct, Initial thought Approach
        if n <= 0:
            return False

        # while not (n & 1):
        #     n //= 2
        
        # return n == 1



        return bin(n).count('1') == 1