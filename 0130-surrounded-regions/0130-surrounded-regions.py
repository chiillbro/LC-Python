class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False] * n for _ in range(m)]

        def dfs(row, col):
            visited[row][col] = True

            for dir_r, dir_c in directions:
                r, c = dir_r + row, dir_c + col
                if not (0 <= r < m) or not (0 <= c < n) or board[r][c] == 'X' or visited[r][c]:
                    continue
                dfs(r, c)
        
        for row in range(m):
            for col in range(n):
                if (row == 0 or col == 0 or row == m - 1 or col == n - 1) and board[row][col] == 'O' and not visited[row][col]:
                    dfs(row, col)
        
        for row in range(1, m):
            for col in range(1, n):
                if board[row][col] == 'O' and not visited[row][col]:
                    board[row][col] = 'X'
        