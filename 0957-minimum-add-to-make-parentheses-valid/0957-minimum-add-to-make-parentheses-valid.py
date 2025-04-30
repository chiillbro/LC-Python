class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s: return ""

        # opens = closes = 0

        # for char in s:
        #     if char == '(':
        #         opens += 1
        #     else:
        #         closes += 1
        
        # return abs(opens - closes)

        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
        
        return len(stack)