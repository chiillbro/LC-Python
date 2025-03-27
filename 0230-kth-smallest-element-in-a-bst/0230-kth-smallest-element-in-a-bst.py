# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # stack = []

        # while True:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return root.val
        #     root = root.right

        while root:
            if not root.left:
                k -= 1
                if k == 0:
                    return root.val
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = root
                    root = root.left
                else:
                    prev.right = None
                    k -= 1
                    if k == 0:
                        return root.val
                    root = root.right 

# ************* Follow Up : If the BST is modified often ****************
# class AugmentedTreeNode:
#     def __init__(self, val=0, left=None, right=None, size=1):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.size = size
# class AugmentedBST:
#     def insert(self, root, val):
#         if not root:
#             return AugmentedTreeNode(val)
#         if val < root.val:
#             root.left = self.insert(root.left, val)
#         if val > root.val:
#             root.right = self.insert(root.right, val)
#         self.size = 1 + self.getSize(root.left) + self.getSize(root.right)
#         return root
#     def getSize(self, node):
#         if not node:
#             return 0
#         return node.size
#     def kthSmallest(self, root, k):
#         leftSize = self.getSize(root.left)
#         if k <= leftSize:
#             return self.kthSmallest(root.left, k)
#         elif k > leftSize + 1:
#             return self.kthSmallest(root.right, k - leftSize - 1)
#         return root.val