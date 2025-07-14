class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        # Recursion
        # @cache
        # def backtrack(cur: str, idx: int):
            
        #     if idx >= len(s):
        #         return True if cur in wordSet else False
            
        #     if cur in wordSet:
        #         if backtrack(s[idx], idx + 1):
        #             return True
            
        #     return backtrack(cur + s[idx], idx + 1)
        

        # return backtrack("", 0)

        # Bottom Up DP

        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
        
        return dp[len(s)]