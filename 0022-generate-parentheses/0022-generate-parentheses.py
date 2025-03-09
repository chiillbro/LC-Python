class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                res.append(''.join(cur))
                return
            
            if open_count < n:
                cur.append('(')
                backtrack(open_count + 1, close_count)
                cur.pop()
            
            if close_count < open_count:
                cur.append(')')
                backtrack(open_count, close_count + 1)
                cur.pop()

        backtrack(0, 0)
        return res
