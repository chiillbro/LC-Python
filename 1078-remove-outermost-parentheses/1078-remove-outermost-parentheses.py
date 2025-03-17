class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []

        start_cnt = end_cnt = 0

        curStart = -1

        for i, p in enumerate(s):
            if p == ')':
                if (not stack or stack[-1] == ')') and start_cnt == end_cnt:
                    curStart = -1
                    end_cnt = 0
                else:
                    end_cnt += 1
                    stack.append(p)
            else:
                if curStart == -1:
                    curStart = i
                    start_cnt = 0
                else:
                    start_cnt += 1
                    stack.append(p)

        return ''.join(stack)
                