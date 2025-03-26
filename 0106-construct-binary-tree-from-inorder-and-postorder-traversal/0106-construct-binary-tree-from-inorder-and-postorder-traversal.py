# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        lu = {num : i for i, num in enumerate(inorder)}

        # def construct(start, end, pIdx):
        #     if start > end:
        #         return None, pIdx

        #     val = postorder[pIdx]
        #     pIdx -= 1

        #     root = TreeNode(val)
        #     index = lu[val]

        #     root.right, pIdx = construct(index +1, end, pIdx)
        #     root.left, pIdx = construct(start, index - 1, pIdx)

        #     return root, pIdx

        # return construct(0, len(postorder) - 1, len(postorder) - 1)[0]

        def construct(postStart, postEnd, inStart, inEnd):
            if postEnd > postStart or inStart > inEnd:
                return
            
            val = postorder[postStart]
            node = TreeNode(val)
            in_index = lu[val]
            numsRight = inEnd - in_index

            node.left = construct(postStart - numsRight - 1, postEnd, inStart, in_index - 1)
            node.right = construct(postStart - 1, postStart - numsRight, in_index + 1, inEnd)
            return node
        
        return construct(len(postorder) - 1, 0, 0, len(inorder) - 1)
            
