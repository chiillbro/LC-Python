class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])


        visited = [[0] * m for _ in range(n)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c):
            visited[r][c] = 1

            for dir_r, dir_c in directions:
                new_r, new_c = dir_r + r, dir_c + c

                if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == "1" and not visited[new_r][new_c]:
                    dfs(new_r, new_c)
        

        islands = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and not visited[row][col]:
                    dfs(row, col)
                    islands += 1
        
        return islands