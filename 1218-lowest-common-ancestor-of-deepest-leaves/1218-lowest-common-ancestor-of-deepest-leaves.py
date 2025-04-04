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
        
        # postorder = []
        # stack1, stack2 = [(0, root)], []
        # depth = 0
        # lca = root

        # while stack1:
        #     depth, current = stack1.pop()
        #     stack2.append((depth, current))
        #     if current.left and current.right:
        #         lca = 
        #     if current.left:
        #         stack1.append((depth + 1, current.left))
        #     if current.right:
        #         stack1.append((depth + 2, current.right))
            
        # while stack2:
        #     postorder.appedn(stack2.pop().val)


        def dfs(root):
            if not root:
                return 0, None

            left, right = dfs(root.left), dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            elif left[0] < right[0]:
                return right[0] + 1, right[1]
            
            return left[0] + 1, root
        
        return dfs(root)[1]
            
