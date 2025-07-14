class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

        self.size = [1] * n
        
        self.comps = n

    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return
        
        if self.size[xRoot] < self.size[yRoot]:
            xRoot, yRoot = yRoot, xRoot
        
        self.parent[yRoot] = xRoot
        self.size[xRoot] += self.size[yRoot]
        self.comps -= 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        extra_edges = 0

        uf = DSU(n)

        for u, v in connections:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
            else:
                extra_edges += 1

        required_edges = uf.comps - 1

        if extra_edges >= required_edges:
            return required_edges
        
        return -1