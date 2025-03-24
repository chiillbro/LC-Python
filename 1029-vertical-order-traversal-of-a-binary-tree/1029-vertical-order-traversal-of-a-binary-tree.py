# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([(root, 0, 0)])

        level_to_col_map = defaultdict(list)

        while queue:
            node, level, col = queue.popleft()
            heappush(level_to_col_map[col], (level, node.val))

            if node.left:
                queue.append((node.left, level + 1, col - 1))
            if node.right:
                queue.append((node.right, level + 1, col + 1))
        
        res = []

        for col in sorted(level_to_col_map.keys()):
            col_vals = []

            while level_to_col_map[col]:
                level, val = heappop(level_to_col_map[col])
                col_vals.append(val)
            
            res.append(col_vals)
        
        return res


