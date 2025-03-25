# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        queue = deque([(root, 0)])
        level_to_node_map = defaultdict(int)

        while queue:
            node, level = queue.popleft()

            if level not in level_to_node_map:
                level_to_node_map[level] = node.val
            
            # if asks left view, just reverse the below if conditions.
            if node.right:
                queue.append((node.right, level + 1))
            
            if node.left:
                queue.append((node.left,level + 1))
        

        return [level_to_node_map[level] for level in sorted(level_to_node_map.keys())]
