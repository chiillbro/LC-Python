class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

        self.size = [1] * n
    
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

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = DSU(n*n)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                cur_cell = i * n + j
                for dir_r, dir_c in directions:
                    new_r, new_c = dir_r + i, dir_c + j

                    if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 1:
                        adj_cell = new_r * n + new_c
                        uf.union(cur_cell, adj_cell)
        
        large_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: continue
                
                pars = set()
                # cur_cell = i * n + j
                for dir_r, dir_c in directions:
                    new_r, new_c = dir_r + i, dir_c + j

                    if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 1:
                        adj_cell = new_r * n + new_c
                        pars.add(uf.find(adj_cell))
                

                cur_size = sum(uf.size[par] for par in pars) + 1

                large_island = max(large_island, cur_size)
        
        if not large_island:
            return n*n
        
        return large_island
                    
