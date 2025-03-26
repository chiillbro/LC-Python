class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_grid = [num for row in grid for num in row]
        if len(flat_grid) == 1:
            return 0
        flat_grid.sort()

        median = flat_grid[len(flat_grid) >> 1]

        res = 0
        for num in flat_grid:
            absolute_value = abs(median - num)
            if absolute_value  % x != 0:
                return -1
            res += absolute_value // x

        return res
