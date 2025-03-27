# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # ** Iterative Approach ** #
        # current = root
        # while current:
        #     if p.val < current.val and q.val < current.val:
        #         current = current.left
        #     elif p.val > current.val and q.val > current.val:
        #         current = current.right
        #     else:
        #         return current

        # ** Recursive Approach ** #

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root