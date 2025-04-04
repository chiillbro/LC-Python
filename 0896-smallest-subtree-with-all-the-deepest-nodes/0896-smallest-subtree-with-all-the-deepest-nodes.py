# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(root: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if not root:
                return 0, None
            
            left, right = dfs(root.left), dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            elif left[0] < right[0]:
                return right[0] + 1, right[1]
            
            return left[0] + 1, root
    
        return dfs(root)[1]