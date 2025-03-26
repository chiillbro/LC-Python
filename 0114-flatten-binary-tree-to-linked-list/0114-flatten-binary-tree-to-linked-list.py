# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # ** Recursive Approach ** #

        if not root: return

        # prev = None

        # def flattenNode(node: Optional[TreeNode]) -> None:
        #     nonlocal prev
        #     if not node:
        #         return
            

        #     flattenNode(node.right)
        #     flattenNode(node.left)

        #     node.right = prev
        #     node.left = None
        #     prev = node
        
        # flattenNode(root)

        # ** Iterative Approach ** #

        # stack = [root]

        # while stack:
        #     node = stack.pop()

        #     if node.right:
        #         stack.append(node.right)
            
        #     if node.left:
        #         stack.append(node.left)
            
        #     if stack:
        #         node.right = stack[-1]
        #         node.left = None

        # ** Morris Traversal Approach ** 

        cur = root

        while cur:
            if cur.left:
                prev = cur.left

                while prev.right:
                    prev = prev.right
                
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            
            cur = cur.right
        