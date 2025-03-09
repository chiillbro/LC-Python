# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 1. Recursive Approach
        # if not root: return 0
        
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # return max(left_depth, right_depth) + 1

        # 2. Iterative Approach

        if not root: return 0

        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth