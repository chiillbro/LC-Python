class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s: return ""

        opens = mismatches = 0

        for char in s:
            if char == '(':
                opens += 1
            else:
                opens -= 1
                if opens < 0:
                    mismatches += 1
                    opens = 0
        
        return opens + mismatches


        # Using Stack: More intuitive

        # stack = []

        # for char in s:
        #     if char == "(":
        #         stack.append(char)
            
        #     else:
        #         if stack and stack[-1] == "(":
        #             stack.pop()
        #         else:
        #             stack.append(char)
        
        # return len(stack)