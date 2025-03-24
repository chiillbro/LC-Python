# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        # ** Iterative Approach using double-ended queue ** #
        res = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

    #     res = []
    #     self._helper(root, 0, res)
    #     return res
    
    # def _helper(self, node: Optional[TreeNode], level: int, res: List[List[int]]) -> None:
    #     if not node:
    #         return
        
    #     if len(res) <= level:
    #         res.append([])
        
    #     res[level].append(node.val)
    #     self._helper(node.left, level + 1, res)
    #     self._helper(node.right, level + 1, res)