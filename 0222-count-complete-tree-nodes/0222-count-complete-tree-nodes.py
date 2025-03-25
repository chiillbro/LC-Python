# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        # ** Naive Approach ** #
        if not root: return 0

        # q = deque([root])
        # res = 0

        # while q:
        #     res += 1
        #     node = q.popleft()
            
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        
        # return res

        # ** Optimal Approach: leveraging the complete binary tree properties **

        left_depth = self._getLeftDepth(root)
        right_depth = self._getRightDepth(root)

        if left_depth == right_depth: # means the sub tree is a perfect binary tree
            return (1 << (left_depth)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    

    def _getLeftDepth(self, node: Optional[TreeNode]) -> int:
        if not node: return 0

        return 1 + self._getLeftDepth(node.left)
    
    def _getRightDepth(self, node: Optional[TreeNode]) -> int:
        if not node: return 0

        return 1 + self._getRightDepth(node.right)