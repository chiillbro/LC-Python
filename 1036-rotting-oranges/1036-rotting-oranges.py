class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        minutes, fresh = 0, 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh:
            for _ in range(len(q)):
                rot_row, rot_col = q.popleft()
                for dr, dc in directions:
                    row, col = rot_row + dr, rot_col + dc
                    if (row < 0 or row >= ROWS or
                        col < 0 or col >= COLS or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append([row, col])
            minutes += 1
        
        return minutes if not fresh else -1

