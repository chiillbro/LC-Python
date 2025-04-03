class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        heap = [(0, 0, 0)]
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0

        while heap:
            min_diff, cur_r, cur_c = heappop(heap)

            if cur_r == m - 1 and cur_c == n - 1:
                return min_diff
            for dr, dc in directions:
                r, c = cur_r + dr, cur_c + dc

                if (0 <= r < m) and (0 <= c < n):
                    max_diff = max(abs(heights[cur_r][cur_c] - heights[r][c]), min_diff)
                    
                    if max_diff < dist[r][c]:
                        dist[r][c] = max_diff
                        heappush(heap, (max_diff, r, c))
        
        return 0
        

