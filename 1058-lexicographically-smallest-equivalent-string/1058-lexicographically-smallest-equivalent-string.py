class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        
        if x_root > y_root:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        n = len(s1)
        uf = UnionFind(26)

        for i in range(n):
            s1_char_val = ord(s1[i]) - 97
            s2_char_val = ord(s2[i]) - 97

            uf.union(s1_char_val, s2_char_val)
        

        res = []

        for char in baseStr:
            char_val = ord(char) - 97
            parent_char_val = uf.find(char_val)

            res.append(chr(parent_char_val + 97))

        return ''.join(res)