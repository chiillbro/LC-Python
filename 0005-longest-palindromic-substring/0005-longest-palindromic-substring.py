class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # Two Pointers, expanding around center, TC: O(N^2), SC: O(1)

        # def expandAroundCenter(i, j):
        #     while i >= 0 and j < n and s[i] == s[j]:
        #         i -= 1
        #         j += 1
            
        #     return s[i+1:j]
        
        # longest = ""
        # for idx in range(n):
        #     p1 = expandAroundCenter(idx, idx)
        #     p2 = expandAroundCenter(idx, idx + 1)

        #     if len(p1) > len(longest):
        #         longest = p1
            
        #     if len(p2) > len(longest):
        #         longest = p2
        
        # return longest


        # DP approach, TC: O(N^2), SC: O(N^2)

        if n < 2:
            return s

        # dp[i][j] represents whether s[i:j] incusively is a palindrome or not
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1

        for L in range(2, n+1):
            for i in  range(n-L+1):
                j = i + L - 1

                if s[i] == s[j]:
                    if L == 2 or dp[i+1][j-1] == True:
                        dp[i][j] = True

                        if L > max_len:
                            start = i
                            max_len = L
        
        return s[start:start+max_len]
        
