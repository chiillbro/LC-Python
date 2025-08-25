class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        max_i, max_j = 0, 0
        min_i, min_j = n, m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
        
        return (max_i - min_i + 1) * (max_j - min_j + 1)