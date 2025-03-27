# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.inorder = []
    #     self.i = -1
    #     while root:
    #         if not root.left:
    #             self.inorder.append(root.val)
    #             root = root.right
            
    #         else:
    #             prev = root.left
    #             while prev.right and prev.right != root:
    #                 prev = prev.right
                
    #             if not prev.right:
    #                 prev.right = root
    #                 root = root.left
    #             else:
    #                 prev.right = None
    #                 self.inorder.append(root.val)
    #                 root = root.right


    # def next(self) -> int:
    #     self.i += 1
    #     return self.inorder[self.i]

    # def hasNext(self) -> bool:
    #     return self.i < len(self.inorder) - 1


    # *** Using Stack: Optimized Solution *** #
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_back(root)
    
    def _push_back(self, node: Optional[TreeNode]) -> None:
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        cur = self.stack.pop()
        self._push_back(cur.right)
        
        return cur.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
            

# ** WE SHOULD NEVER IMPLEMENT THE FIRST APPROACH FOR THIS KIND OF PROBLEMS, WHAT I MEAN IS ITERATORS SHOULD NEVER COMPUTE THE RESULTS BEFOREHAND THAT THEY ARE GOING TO USED LATER, ITERATORS ARE MEANT TO LAZILY GIVE THE CURRENT OUTPUT WHEN ASKED

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()