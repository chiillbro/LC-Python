class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit_repr = format(n, "b")


        return all(bit_repr[i-1] != bit_repr[i] for i in range(1, len(bit_repr)))