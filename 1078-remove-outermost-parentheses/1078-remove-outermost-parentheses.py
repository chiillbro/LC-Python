class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        depth = 0

        for char in s:
            if char == ')':
                depth -= 1
                if depth > 0:
                    stack.append(char)
            else:
                if depth > 0:
                    stack.append(char)
                depth += 1

        return ''.join(stack)
                