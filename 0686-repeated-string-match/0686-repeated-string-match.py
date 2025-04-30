class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)

        n = m // n

        na = a * n

        if b in na:
            return n
        
        na += a

        if b in na:
            return n + 1
        
        na += a

        if b in na:
            return n + 2
        
        return -1