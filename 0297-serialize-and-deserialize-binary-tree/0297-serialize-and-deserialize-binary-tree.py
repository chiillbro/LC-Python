# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # hardcore null node indicators
        # null : -
        if not root:
            return ""
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('-')
            # res.append(node.val)

            # if node.left:
            #     queue.append(node.left)
            # else:
            #     res.append('-')
            
            # if node.right:
            #     queue.append(node.right)
            # else:
            #     res.append('-')

        return ','.join(map(str, res))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        root = TreeNode()

        s = data.split(',')
        rootVal = s[0]
        root.val = int(rootVal)
        i = 1
        queue = deque([root])

        while i < len(s):
            left = s[i]
            i += 1
            node = queue.popleft()

            if left == '-':
                node.left = None
            else:
                left_node = TreeNode(int(left))
                node.left = left_node
                queue.append(node.left)


            right = s[i]
            i += 1
            if right == '-':
                node.right = None
            else:
                right_node = TreeNode(int(right))
                node.right = right_node
                queue.append(node.right)
            
        return root



            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))