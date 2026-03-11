class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = n | 1

        for i in range(5):
            mask |= mask >> (1 << i)
        
        return n ^ mask