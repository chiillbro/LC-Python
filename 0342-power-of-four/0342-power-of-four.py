class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n == 1:
        #     return True
        
        # if n < 4:
        #     return False
        
        # LARGEST_FOUR_POWER = 4**16

        # return LARGEST_FOUR_POWER % n == 0 and (n-1) % 3 == 0

        return n > 0 and n.bit_count() == 1 and (n-1) % 3 == 0