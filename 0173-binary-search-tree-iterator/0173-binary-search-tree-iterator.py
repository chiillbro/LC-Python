# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.i = -1
        cur = root
        while cur:
            if not cur.left:
                self.inorder.append(cur.val)
                cur = cur.right
            
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    self.inorder.append(cur.val)
                    cur = cur.right


    def next(self) -> int:
        self.i += 1
        return self.inorder[self.i]

    def hasNext(self) -> bool:
        return self.i < len(self.inorder) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()