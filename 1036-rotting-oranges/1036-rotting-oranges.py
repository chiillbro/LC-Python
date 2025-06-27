class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])


        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        grid_copy = grid.copy()

        queue = deque()
        minutes, fresh = 0, 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while queue and fresh:
            level = len(queue)

            for _ in range(level):
                cur_r, cur_c = queue.popleft()

                for d_r, d_c in directions:
                    r, c = cur_r + d_r, cur_c + d_c

                    if 0 <= r < n and 0 <= c < m and grid_copy[r][c] == 1:
                        grid_copy[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))
            
            minutes += 1


        return minutes if fresh == 0 else -1