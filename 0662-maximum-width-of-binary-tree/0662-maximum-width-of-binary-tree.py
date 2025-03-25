# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        ans = 0

        while queue:
            level_start = queue[0][1]
            level_end = queue[-1][1]

            ans = max(ans, level_end - level_start + 1)
            for _ in range(len(queue)):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return ans