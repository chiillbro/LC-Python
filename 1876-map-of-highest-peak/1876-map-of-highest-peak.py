class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque()

        for row in range(m):
            for col in range(n):
                if isWater[row][col] == 1:
                    visited[row][col] = True
                    queue.append((row, col, 0))
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = [[0]* n for _ in range(m)]

        while queue:
            row, col, height = queue.popleft()
            res[row][col] = height

            for dir_r, dir_c in directions:
                r, c = dir_r + row, dir_c + col

                if (0 <= r < m) and (0 <= c < n) and not visited[r][c]:
                    visited[r][c] = True
                    queue.append((r, c, height + 1))
        
        return res