# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == key:
            return self.delete(root)
        
        cur = root
        while cur:
            if cur.val > key:
                if cur.left and cur.left.val == key:
                    cur.left = self.delete(cur.left)
                else:
                    cur = cur.left
            else:
                if cur.right and cur.right.val == key:
                    cur.right = self.delete(cur.right)
                else:
                    cur = cur.right
        return root
    
    def delete(self, node):
        if not node.left:
            return node.right
        
        if not node.right:
            return node.left
        

        last_right = self.findRightMost(node.left)
        last_right.right = node.right

        return node.left
    
    def findRightMost(self, node):
        while node.right:
            node = node.right
        
        return node
