# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0
                
            left, right = dfs(node.left), dfs(node.right)

            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return res