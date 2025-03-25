# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        child_to_parent = defaultdict(TreeNode) # not common for child parent nodes mapping
        # child_to_parent = {}
        self._markParent(root, child_to_parent)

        queue = deque([target])
        visited = set()
        visited.add(target)
        cur_lvl = 0

        while queue:
            if cur_lvl == k: break
            cur_lvl += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                
                if node in child_to_parent and child_to_parent[node] not in visited:
                    visited.add(child_to_parent[node])
                    queue.append(child_to_parent[node])
        
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur.val)
        
        return res

        
    def _markParent(self, root: TreeNode, child_to_parent: Dict[TreeNode, TreeNode]) -> None:
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    child_to_parent[node.left] = node
                    queue.append(node.left)
                
                if node.right:
                    child_to_parent[node.right] = node
                    queue.append(node.right)
