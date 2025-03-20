class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        n = len(digits)
        if not digits:
            return []
        if n == 1:
            return list(num_to_char[digits])
        
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