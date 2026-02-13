# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def _check_height(node):
            if not node:
                return 0
            
            left_check = _check_height(node.left)
            if left_check == -1:
                return -1

            right_check = _check_height(node.right)
            if right_check == -1:
                return -1

            if abs(left_check - right_check) > 1:
                return -1

            return 1 + max(left_check, right_check)

        return _check_height(root) != -1
            

