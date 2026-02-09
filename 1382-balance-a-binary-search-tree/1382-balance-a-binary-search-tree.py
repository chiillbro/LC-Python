# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []


        def _inorder_traversal(node):
            nonlocal arr

            if node:
            
                _inorder_traversal(node.left)
            
                arr.append(node.val)

                _inorder_traversal(node.right)

        
        _inorder_traversal(root)

        return self._build_balanced_bst(arr, 0, len(arr) - 1)


    def _build_balanced_bst(self, arr, start, end):
        if start > end:
            return

        mid = (start + end) // 2

        node = TreeNode(arr[mid])

        node.left = self._build_balanced_bst(arr, start, mid - 1)
        node.right = self._build_balanced_bst(arr, mid + 1, end)

        return node

        

