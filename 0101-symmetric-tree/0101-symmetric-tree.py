# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # ** Recursive Approach ** #

        def _isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False

            return _isMirror(left.left, right.right) and _isMirror(right.left, left.right)
        
        return _isMirror(root, root)