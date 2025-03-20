class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        n = len(digits)
        if not digits:
            return []
        if n == 1:
            return num_to_char[digits]
        
        res = []
        
        def backtrack(i, sol):
            if i == n:
                res.append(''.join(sol))
                return
            
            for c in num_to_char[digits[i]]:
                sol.append(c)
                backtrack(i + 1, sol)
                sol.pop()
            

        backtrack(0, [])
        return res