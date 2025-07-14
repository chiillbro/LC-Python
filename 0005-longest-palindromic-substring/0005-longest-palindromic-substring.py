class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expandAroundCenter(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            
            return s[i+1:j]
        
        longest = ""
        for idx in range(n):
            p1 = expandAroundCenter(idx, idx)
            p2 = expandAroundCenter(idx, idx + 1)

            if len(p1) > len(longest):
                longest = p1
            
            if len(p2) > len(longest):
                longest = p2
        
        return longest