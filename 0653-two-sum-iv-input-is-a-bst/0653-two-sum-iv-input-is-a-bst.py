# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        compl_set = set()

        # ** Recursive Approach ** #

        # def helper(node):
        #     if not node: return False

        #     if k - node.val in compl_set:
        #         return True
            
        #     compl_set.add(node.val)
            
        #     return helper(node.left) or helper(node.right)
        
        # return helper(root)



        # *** Iterative Approach using BFS *** #
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if k - node.val in compl_set:
                return True
            
            compl_set.add(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return False