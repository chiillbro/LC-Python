# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # Greedy, Dynamic Programming

        # def dfs(node):
        #     if not node: return 0, 0

        #     l1, l2 = dfs(node.left)
        #     r1, r2 = dfs(node.right)

        #     rob = node.val + l2 + r2
        #     not_rob = max(l1, l2) + max(r1, r2)

        #     return rob, not_rob
        
        # return max(dfs(root))


        # Brute Recursion

        # Memoization

        memo = {}
        def helper(node):
            if not node: return 0

            if node in memo:
                return memo[node]
        
            val = 0

            if node.left:
                val += helper(node.left.left) + helper(node.left.right)
            
            if node.right:
                val += helper(node.right.left) + helper(node.right.right)
            
            memo[node] = max(val + node.val, helper(node.left) + helper(node.right))

            return memo[node]
        

        return helper(root)