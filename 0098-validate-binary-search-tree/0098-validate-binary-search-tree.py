# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # prev: Optiona[TreeNode] = None

        # def helper(node: Optional[TreeNode]) -> bool:
        #     nonlocal prev
        #     if not node:
        #         return True
            
        #     if not helper(node.left):
        #         return False
            
        #     if prev and prev.val >= node.val:
        #         return False
            
        #     prev = node

        #     return helper(node.right)

        # return helper(root)

        # ** Second Approach: check recursively whether a node's val is in the range of values it should be 

        def helper(node: Optional[TreeNode], cur_min, cur_max) -> bool:
            if not node: return True

            if not (cur_min < node.val < cur_max):
                return False

            if not helper(node.left, cur_min, node.val):
                return False
            
            if not helper(node.right, node.val, cur_max): 
                return False
            
            return True
            
        return helper(root, float('-inf'), float('inf'))