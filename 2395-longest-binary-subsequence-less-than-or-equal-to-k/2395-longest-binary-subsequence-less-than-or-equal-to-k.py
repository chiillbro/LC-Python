class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n = len(s)

        val = 0
        j = n-1
        while val <= k and j >= 0:
            if s[j] == '1':
                set_bit = n - j -1
                print("set_bit, val", set_bit, 1 << set_bit)
                val += 1 << set_bit
            
            j -= 1
            print("val at j", val, j)
            
        print("val", val)

        print("j", j)
        
        if j == -1 and val <= k:
            return n
        
        j += 1
        
        while j < n-1 and s[j+1] == '0':
            j += 1

        print("at last j", j)
        
        zeroes_till_j = 0

        for i in range(j+1):
            if s[i] == '0':
                zeroes_till_j += 1
        
        print("zeroes_till_j", zeroes_till_j)
        
        return n - j - 1 + zeroes_till_j