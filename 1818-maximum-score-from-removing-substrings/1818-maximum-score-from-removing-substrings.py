class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)

        priority_pattern = 'ab' if x > y else 'ba'

        # i = 0
        # stack = []
        score = 0

        # print("priority_pattern", priority_pattern)

        # def backtrack():
        #     nonlocal score
        #     while len(stack) >= 2:
        #         second = stack.pop()
        #         first = stack.pop()
        #         pattern = first + second
        #         if pattern == priority_pattern:
        #             score += max(x, y)
        #         elif pattern == priority_pattern[::-1]:
        #             score += min(x, y)
            
        #     stack.clear()

        # while i < n:
        #     if s[i] in 'ab':

        #         if stack and s[i] == priority_pattern[1] and stack[-1] == priority_pattern[0]:
        #             stack.pop()
        #             score += max(x, y)
        #         else:
        #             stack.append(s[i])

        #     elif len(stack) > 1:
        #         backtrack()

        #     print("stack at", i, stack)
            
        #     i += 1
        
        # print("stack", stack)
        # backtrack()



        def remove_pattern(st, pat, val):
            nonlocal score
            stack = []
            a, b = pat
            for char in st:
                if stack and stack[-1] == a and char == b:
                    stack.pop()
                    score += val
                
                else:
                    stack.append(char)
            
            return ''.join(stack)
        
        rem = remove_pattern(s, priority_pattern, max(x, y))
        remove_pattern(rem, priority_pattern[::-1], min(x, y))

        return score