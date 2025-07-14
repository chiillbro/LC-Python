class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        # Recursion
        @cache
        def backtrack(cur: str, idx: int):
            
            if idx >= len(s):
                return True if cur in wordSet else False
            
            if cur in wordSet:
                if backtrack(s[idx], idx + 1):
                    return True
            
            return backtrack(cur + s[idx], idx + 1)
        

        return backtrack("", 0)