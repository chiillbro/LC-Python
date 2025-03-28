# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # ** Iterative Approach using stack (inorder) ** #
        
        # stack = []
        # prev = first = last = None
        # node = root

        # while stack or node:
        #     while node:
        #         stack.append(node)
        #         node = node.left

        #     node = stack.pop()

        #     if prev and node.val < prev.val:
        #         if not first:
        #             first = prev
        #         last = node
            
        #     prev = node
        #     node = node.right

        # if first and last:
        #     first.val, last.val = last.val, first.val


        # ** Morris Traversal: constant space Approach ** #

        prev = first = last = None
        cur = root
        
        while cur:
            if not cur.left:
                if prev and cur.val < prev.val:
                    if not first:
                        first = prev
                    last = cur
                prev = cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if prev and cur.val < prev.val:
                        if not first:
                            first = prev
                        last = cur
                    prev = cur
                    cur = cur.right
            
        if first and last:
            first.val, last.val = last.val, first.val

        # ** Recursive Approach ** #
        # prev = first = last = None
        # def inorder(node: Optional[TreeNode]) -> None:
        #     nonlocal prev, first, last
        #     if not node: return None

        #     inorder(node.left)

        #     if prev and node.val < prev.val:
        #         if not first:
        #             first = prev
        #         last = node
            
        #     prev = node
        #     inorder(node.right)
        
        # inorder(root)

        # if first and last:
        #     first.val, last.val = last.val, first.val