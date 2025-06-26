# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:
    def __init__(self, root, forward=True):
        self.stack = []
        self.forward = forward
        self._push(root)
    
    def _push(self, node):
        while node:
            self.stack.append(node)
            node = node.left if self.forward else node.right
        

    def has_next(self):
        return bool(self.stack)
    

    def next(self):
        node = self.stack.pop()

        nxt = node.right if self.forward else node.left
        self._push(nxt)
        return node.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        # Approach 1, DFS + Set, TC: O(n), SC: O(n)
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



        # Approach 2, Inorder + Two pointers, TC: O(n), SC: O(n)
        # arr = []

        # def inorder(node):
        #     if not node: return

        #     inorder(node.left)

        #     arr.append(node.val)

        #     inorder(node.right)
        
        # inorder(root)

        # i, j = 0, len(arr) - 1

        # while i < j:
        #     cur_sum = arr[i] + arr[j]

        #     if cur_sum == k:
        #         return True
            
        #     if cur_sum > k:
        #         j -= 1
        #     else:
        #         i += 1
        
        # return False


        # Approach 3: BST Two Iterator, TC: O(n), SC: O(h) h = height of the tree, More optimal

        left_iter = BSTIterator(root)
        right_iter = BSTIterator(root, forward=False)


        i, j = left_iter.next(), right_iter.next()

        while i < j:
            cur = i + j

            if cur == k: return True

            if cur < k:
                if not left_iter.has_next(): return False

                i = left_iter.next()
            
            else:
                if not right_iter.has_next(): return False

                j = right_iter.next()
        
        return False