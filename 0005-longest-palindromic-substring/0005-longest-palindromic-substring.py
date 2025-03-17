class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        N = len(s)

        def expandAroundCenter(left, right):
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]
        
        for i in range(N):
            p1 = expandAroundCenter(i, i)
            p2 = expandAroundCenter(i, i + 1)

            if len(p1) > len(longest):
                longest = p1
            
            if len(p2) > len(longest):
                longest = p2

        return longest