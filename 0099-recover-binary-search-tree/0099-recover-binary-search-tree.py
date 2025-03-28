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
        # queue = deque([root])
        # first, second = None, None

        # while queue:
        #     node = queue.popleft()
        #     if node.left and node.left.val > node.val:
        #         if not first:
        #             first, second = node, node.left
        #         else:
        #             if first.val > node.val:
        #                 first = 
        #     elif node.right and node.right.val < node.val:
        #         if not first:
        #             first, second = node, node.left
        #         else:
        #             if first.val

        first = middle = last = None
        prev = TreeNode(float('-inf'))
        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal prev, first, middle, last
            if not node: return None

            inorder(node.left)

            if node.val < prev.val:
                if not first:
                    first = prev
                    middle = node
                else:
                    last = node
            
            prev = node
            inorder(node.right)
        
        inorder(root)

        if first and last:
            first.val, last.val = last.val, first.val
        elif first and middle:
            first.val, middle.val = middle.val, first.val
                