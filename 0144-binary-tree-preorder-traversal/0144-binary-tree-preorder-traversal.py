# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ** Iterative Approach ** #
        if not root: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res

        # ** Recursive Approach ** #

         # pre = []
        # self._helper(root, pre)
        # return pre
        # ** PRO ** #
        return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    

    # ** NOOB ** #
    # def _helper(self, root, path):
    #     if not root:
    #         return
    #     path.append(root.val)
    #     self._helper(root.left, path)
    #     self._helper(root.right,path)