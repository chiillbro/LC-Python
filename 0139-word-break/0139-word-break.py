class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        # ** Top Down Approach : Recursion ** #
        memo = defaultdict(bool)
        def backtrack(cur, index):
            key = cur + "_" + str(index)
            if key in memo:
                return memo[key]
            if index == len(s):
                return True if cur in word_set else False

            if cur in word_set:
                if backtrack(s[index], index + 1):
                    memo[key] = True
                    return True
            
            memo[key] = backtrack(cur + s[index], index + 1)
            return memo[key]
        

        return backtrack("", 0)

        #. ** Bottom Up Approach : DP ** #
        # dp = [False] * (len(s) + 1)
        # dp[0] = True

        # for i in range(1, len(s) + 1):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in word_set:
        #             dp[i] = True
        # return dp[len(s)]
