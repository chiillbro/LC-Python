# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def _calculateSum(node: Optional[TreeNode]) -> int:
            nonlocal max_sum

            if not node:
                return 0

            left_gain = max(_calculateSum(node.left), 0)
            right_gain = max(_calculateSum(node.right), 0)

            max_sum = max(max_sum, left_gain + node.val + right_gain)

            return node.val + max(left_gain, right_gain)
        
        _calculateSum(root)
        return max_sum