class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        gap = 1
        last_bit_found = 0

        while n > 0:
            if n & 1:
                if last_bit_found:
                    ans = max(ans, gap)
                else:
                    last_bit_found = 1
                gap = 1
            else:
                gap += 1
            
            n >>= 1
        

        return ans
