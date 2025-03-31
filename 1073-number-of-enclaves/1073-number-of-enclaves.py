class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = [[False] * n for _ in range(m)]

        def dfs(row, col):
            visited[row][col] = True

            for dir_r, dir_c in directions:
                r, c = dir_r + row, dir_c + col

                if (0 <= r < m) and (0 <= c < n) and grid[r][c] and not visited[r][c]:
                    dfs(r, c)
        

        for row in range(m):
            for col in range(n):
                if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and grid[row][col] and not visited[row][col]:
                    dfs(row, col)
        
        res = 0
        for row in range(1, m):
            for col in range(1, n):
                if row == m - 1 or col == n - 1:
                    continue
                if grid[row][col] and not visited[row][col]:
                    res += 1
        
        return res