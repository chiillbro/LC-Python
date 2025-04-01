class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        # ** Recursive Top-Down Approach ** #
        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= n: return 0

            pts, skip = questions[i]
            return max(pts+dfs(i + skip + 1), dfs(i + 1))
        
        return dfs(0)