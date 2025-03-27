# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev: Optiona[TreeNode] = None

        def helper(node: Optional[TreeNode]) -> bool:
            nonlocal prev
            if not node:
                return True
            
            if not helper(node.left):
                return False
            
            if prev and prev.val >= node.val:
                return False
            
            prev = node

            return helper(node.right)

        return helper(root)