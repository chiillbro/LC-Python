# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        compl_set = set()

        def helper(node, value):
            if value in compl_set:
                return True
            
            compl_set.add(node.val)
            
            if node.left and helper(node.left, k - node.left.val):
                return True
            elif node.right and helper(node.right, k - node.right.val):
                return True
            
            return False
        
        return helper(root, k - root.val)

        # cur = root
        # while cur:
        #     if k - cur.val in compl_set:
        #         return True
        #     compl_set.add(cur.val)
        #     if k - cur.val > cur.val:
        #         cur = cur.right
        #     else:
        #         cur = cur.left
        # return False


