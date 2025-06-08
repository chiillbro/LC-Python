class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x: # If x is not its own parent
            # Recursively find the true parent of x's parent (self.parent[x])
            # AND make x point DIRECTLY to that true parent.
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x] # Return the true parent

    def union(self, x, y): # x, y are integers 0-25
        x_root = self.find(x) # Find representative of x's group (e.g., 'a')
        y_root = self.find(y) # Find representative of y's group (e.g., 'c')

        if x_root == y_root:
            return # Already in the same group
        
        # Merge by making the lexicographically smaller character the new parent
        # Since 0='a', 1='b', smaller integer means smaller char
        if x_root > y_root: # if char for x_root > char for y_root (e.g., 'c' > 'a')
            self.parent[x_root] = y_root # Make y_root (e.g. 'a') the parent of x_root (e.g. 'c')
                                    # So 'a' becomes the representative for 'c's group.
        else:
            self.parent[y_root] = x_root

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        n = len(s1)
        uf = UnionFind(26)

        for i in range(n):
            s1_char_val = ord(s1[i]) - 97
            s2_char_val = ord(s2[i]) - 97

            uf.union(s1_char_val, s2_char_val) # Union their sets. The Union op ensures
                                          # the new parent is the smaller char.
        

        res = []

        for char in baseStr:
            char_val = ord(char) - 97
            parent_char_val = uf.find(char_val)

            res.append(chr(parent_char_val + 97))

        return ''.join(res)