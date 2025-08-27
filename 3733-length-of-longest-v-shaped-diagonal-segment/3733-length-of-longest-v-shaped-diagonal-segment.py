class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        nx = {
            1 : 2,
            2: 0,
            0: 2
        }

        @cache
        def dp(i, j, x, d, k):
            if not (0 <= i < n and 0 <= j < m):
                return 0
            
            if grid[i][j] != x:
                return 0

            
            res = dp(i + directions[d][0], j + directions[d][1], nx[x], d, k) + 1

            if k > 0:
                d2 = (d + 1) % 4
                res2 = dp(i + directions[d2][0], j + directions[d2][1], nx[x], d2, 0) + 1
                res = max(res2, res)
            
            return res




        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cur = max(dp(i, j, 1, d, 1) for d in range(4))
                    res = max(cur, res)
        
        return res