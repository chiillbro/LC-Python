class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []

        depth = 0

        curStart = -1

        for i, p in enumerate(s):
            if p == ')':
                if (not stack or stack[-1] == ')') and not depth:
                    curStart = -1
                    depth = 0
                else:
                    depth -= 1
                    stack.append(p)
            else:
                if curStart == -1:
                    curStart = i
                else:
                    depth += 1
                    stack.append(p)

        return ''.join(stack)
                