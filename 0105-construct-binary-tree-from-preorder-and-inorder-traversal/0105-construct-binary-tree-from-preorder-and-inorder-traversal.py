# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        lu = {}

        for i, n in enumerate(inorder):
            lu[n] = i

        # def construct(start, end, pIdx):
        #     if start > end:
        #         return None, pIdx
            
        #     val = preorder[pIdx]
        #     pIdx += 1

        #     root = TreeNode(val)
        #     index = lu[val]

        #     root.left, pIdx = construct(start, index - 1, pIdx)
        #     root.right, pIdx = construct(index+1, end, pIdx)

        #     return root, pIdx
        
        # return construct(0, len(preorder) - 1, 0)[0]

        def construct(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return
            
            val = preorder[preStart]
            node = TreeNode(val)
            in_index = lu[val]
            nums_left = in_index - inStart

            node.left = construct(preStart + 1, preStart + nums_left, inStart, in_index - 1)
            node.right = construct(preStart + 1 + nums_left, preEnd, in_index + 1, inEnd)

            return node
        
        return construct(0, len(preorder) - 1, 0, len(inorder) - 1)
