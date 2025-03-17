class Solution:
    def maxDepth(self, s: str) -> int:
        
        cur_depth = max_depth = 0

        for char in s:
            if char == '(':
                cur_depth += 1
            elif char == ')':
                max_depth = max(max_depth, cur_depth)
                cur_depth -= 1
        
        return max_depth
