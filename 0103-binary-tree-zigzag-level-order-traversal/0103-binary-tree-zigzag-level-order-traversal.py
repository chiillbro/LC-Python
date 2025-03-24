# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # if not root:
        #     return []

        # ** Iterative Approach ** #
        # res = []
        # queue = deque([root])
        # leftToRight = True

        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     if not leftToRight:
        #         level.reverse()
            
        #     leftToRight = not leftToRight
        #     res.append(level)
        
        # return res


        # ** Recursive Approach ** #

        res = []
        def helper(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return
            
            if level == len(res):
                res.append([])

            
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        helper(root, 0)
        return res
        