# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isIdentical(root, subRoot):
            return True
        
        return self.isIdentical(root.left, subRoot) or self.isIdentical(root.right, subRoot)
    
    def isIdentical(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        
        return self.isIdentical(node1.left, node2.left) and self.isIdentical(node1.right, node2.right)