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
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        rows_map, cols_map = defaultdict(list), defaultdict(list)

        for idx, (row, col) in enumerate(stones):
            rows_map[row].append(idx)
            cols_map[col].append(idx)
    
        uf = DSU(n)

        for bucket in rows_map.values():
            first = bucket[0]

            for second in bucket[1:]:
                uf.union(first, second)
            
        for bucket in cols_map.values():
            first = bucket[0]
            
            for second in bucket[1:]:
                uf.union(first, second)
        
        unique_roots = {uf.find(idx) for idx in range(n)}

        return n - len(unique_roots)

        # matching_stones = defaultdict(list)

        # for r, c in stones:
        #     pattern1, pattern2 = (r, "*"), ("*", c)

        #     matching_stones[pattern1].append((r, c))
        #     matching_stones[pattern2].append((r, c))

        # max_cell_val = 0

        # max_col = max([col for _, col in stones]) + 1

        # for r, c in stones:
        #     cell = r * max_col + c
        #     max_cell_val = max(max_cell_val, cell)
        #     # stones_set.add((r, c))
        
        # uf = DSU(max_cell_val + 1)
        
        # for r, c in stones:
        #     pattern1 = (r, "*")
        #     pattern2 = ("*", c)
        #     cur_cell = r * max_col + c
        #     for adj_r, adj_c in matching_stones[pattern1]:
        #         adj_cell = adj_r * max_col + adj_c
        #         uf.union(cur_cell, adj_cell)

        #     for adj_r, adj_c in matching_stones[pattern2]:
        #         adj_cell = adj_r * max_col + adj_c
        #         uf.union(cur_cell, adj_cell)
        
        # cells_can_be_removed = 0
        # for r, c in stones:
        #     cur_cell = r * max_col + c

        #     if uf.find(cur_cell) == cur_cell:
        #         cells_can_be_removed += uf.size[cur_cell] - 1
        
        # return cells_can_be_removed