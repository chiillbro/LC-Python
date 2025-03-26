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

        s = data.split(',')
        root = TreeNode(int(s[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(s):
            node = queue.popleft()

            if s[i] != '-':
                left_node = TreeNode(int(s[i]))
                node.left = left_node
                queue.append(node.left)
            i += 1


            if s[i] != '-':
                right_node = TreeNode(int(s[i]))
                node.right = right_node
                queue.append(node.right)
            i += 1
            
        return root



            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))