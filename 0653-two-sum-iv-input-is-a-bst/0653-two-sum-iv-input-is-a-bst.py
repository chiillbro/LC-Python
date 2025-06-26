# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # seen = set()

        # stack = [root]

        # while stack:
        #     cur = stack.pop()

        #     compliment = k - cur.val

        #     if compliment in seen:
        #         return True
            
        #     seen.add(cur.val)
        #     if cur.left:
        #         stack.append(cur.left)
            
        #     if cur.right:
        #         stack.append(cur.right)
        
        # return False

        arr = []

        def inorder(node):
            if not node: return

            inorder(node.left)

            arr.append(node.val)

            inorder(node.right)
        
        inorder(root)
        
        # print("arr", arr)

        i, j = 0, len(arr) - 1

        while i < j:
            cur_sum = arr[i] + arr[j]

            if cur_sum == k:
                return True
            
            if cur_sum > k:
                j -= 1
            else:
                i += 1
        
        return False
