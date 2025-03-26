# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ** Iterative Approach *8 #

        # stack, res = [], []
        # cur = root
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
            
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     cur = cur.right
        
        # return res

        # ** Recursive Approach ** #
        # return [] if not root else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


        # ** Space Optimized Approach: Morris Traversal ** #

        res = []

        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    res.append(cur.val)
                    cur = cur.right
            
        
        return res
