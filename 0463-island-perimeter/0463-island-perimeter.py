class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    perimeter += 4
                    for d_r, d_c in directions:
                        row, col = r + d_r, c + d_c
                        if 0 <= row < m and 0 <= col < n and grid[row][col]:
                            perimeter -= 1
        
        return perimeter
