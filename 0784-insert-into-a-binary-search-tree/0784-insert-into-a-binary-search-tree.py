# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        # ** Recursive Approach ** #

        def insert(node):
            if not node: return

            if node.val < val:
                if not node.right:
                    node.right = new_node
                    return
                else:
                    insert(node.right)
            else:
                if not node.left:
                    node.left = new_node
                    return
                else:
                    insert(node.left)
        
        insert(root)
        return root


        # ** Iterative Approach ** #
        # if not root:
        #     return new_node
        # cur = root

        # while cur:
        #     if cur.val < val:
        #         if not cur.right:
        #             cur.right = new_node
        #             return root
        #         else:
        #             cur = cur.right
        #     else:
        #         if not cur.left:
        #             cur.left = new_node
        #             return root
        #         else:
        #             cur = cur.left