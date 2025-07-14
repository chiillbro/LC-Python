class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0
        def expandAroundCenter(i, j):
            nonlocal count
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1


        for center in range(n):
            expandAroundCenter(center, center)
            expandAroundCenter(center, center + 1)
        
        return count