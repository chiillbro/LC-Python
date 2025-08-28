class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        if n == 1:
            return grid

        res = grid[::]

        def helper(r, c, is_bottom_left):
            cells = []
            vals = []
            while r < n and c < n:
                cells.append((r, c))
                vals.append(grid[r][c])
                r += 1
                c += 1
            
            vals.sort()
            if is_bottom_left:
                vals.reverse()
            
            for i, (r, c) in enumerate(cells):
                res[r][c] = vals[i]

        for c in range(1, n):
            helper(0, c, 0)
        
        for r in range(n):
            helper(r, 0, 1)
        
        return res
