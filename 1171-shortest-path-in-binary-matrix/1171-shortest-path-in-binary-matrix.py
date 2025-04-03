class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        if n == 1 and not grid[0][0]:
            return 1

        # visited = [[False] * n for _ in range(n)]
        dist = [[float("inf")] * n for _ in range(n)]
        dist[0][0] == 1
        # visited[0][0] = True
        heap = [(1, 0, 0)]

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        while heap:
            distance, cur_row, cur_col = heappop(heap)
            
            for dr, dc in directions:
                new_r, new_c = cur_row + dr, cur_col + dc

                if (0 <= new_r < n) and (0 <= new_c < n) and dist[new_r][new_c] == float("inf") and not grid[new_r][new_c]:
                    if distance + 1 < dist[new_r][new_c]:
                        dist[new_r][new_c] = distance + 1
                        heappush(heap, (distance + 1, new_r, new_c))
        

        return dist[n-1][n-1] if dist[n-1][n-1] != float("inf") else -1