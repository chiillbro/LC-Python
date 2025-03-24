# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain = helper(node.left)
            right_gain = helper(node.right)

            # Ignore negative sums
            left_gain = max(left_gain, 0)
            right_gain = max(right_gain, 0)

            # Update max_sum considering the current node as root of a path
            max_sum = max(max_sum, node.val + left_gain + right_gain)
            
            # Return max gain from this node
            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        helper(root)
        return max_sum