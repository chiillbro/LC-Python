class Solution:
    def reverseBits(self, n: int) -> int:
        def reverse(v, length):
            if length == 1:
                return v & 1
            

            half = length >> 1
            mask = (1 << half) - 1

            low, high = v & mask, v >> half

            return (reverse(low, half) << half) | reverse(high, half)
        

        return reverse(n, 32)