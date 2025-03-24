# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        res = []
        queue = deque([root])
        cur = 0

        while queue:
            level = []
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                temp.append(node)
            
            while temp:
                node = temp.pop()
                if not cur:
                    if node.right:
                        queue.append(node.right)
                    
                    if node.left:
                        queue.append(node.left)
                else:
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)

            
            cur = 1 if not cur else 0
            res.append(level)
        
        return res

        