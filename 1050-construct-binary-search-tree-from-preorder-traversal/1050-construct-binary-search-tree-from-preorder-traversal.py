# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        self.i = 0

        def helper(lower, upper):
            if self.i == len(preorder) or not (lower < preorder[self.i] < upper):
                return None
            

            val = preorder[self.i]
            self.i += 1
            node = TreeNode(val)
            node.left = helper(lower, val)
            node.right = helper(val, upper)

            return node
        

        return helper(float('-inf'), float('inf'))