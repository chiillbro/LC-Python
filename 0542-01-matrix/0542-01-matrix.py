class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        visited = [[False] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    visited[row][col] = True
                    queue.append((row, col, 0))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = mat[:]
        while queue:
            row, col, dist = queue.popleft()
            if mat[row][col] == 1:
                res[row][col] = dist

            for dir_r, dir_c in directions:
                r, c = dir_r + row, dir_c + col
                if (0 <= r < m) and (0 <= c < n) and not visited[r][c]:
                    visited[r][c] = True
                    queue.append((r, c, dist + 1))

        return res