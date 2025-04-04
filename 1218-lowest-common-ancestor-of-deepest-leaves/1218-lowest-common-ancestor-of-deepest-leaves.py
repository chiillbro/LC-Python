# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # ** Approach 1: Using Level Order Traversal (BFS) ** #

        queue = deque([root])
        parent = {root: None}

        while queue:
            level = []

            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current)
                if current.left:
                    parent[current.left] = current
                    queue.append(current.left)
                
                if current.right:
                    parent[current.right] = current
                    queue.append(current.right)
            
            if not queue:
                deepest = level
        
        if len(deepest) == 1:
            return deepest[0]
        
        while len({node for node in deepest}) > 1:
            deepest = [parent[node] for node in deepest]
        
        return deepest[0]


        # ** Approach 2 : Using DFS - Post-Order Traversal(recursive) ** #

        # def dfs(root):
        #     if not root:
        #         return 0, None

        #     left, right = dfs(root.left), dfs(root.right)

        #     if left[0] > right[0]:
        #         return left[0] + 1, left[1]
        #     elif left[0] < right[0]:
        #         return right[0] + 1, right[1]
            
        #     return left[0] + 1, root
        
        # return dfs(root)[1]