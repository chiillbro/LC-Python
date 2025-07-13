class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])

        dist = [[math.inf] * m for _ in range(n)]

        dist[0][0] = 0

        pq = [(0, 0, 0)]

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while pq:
            cur_effort, cur_r, cur_c = heappop(pq)

            if cur_r == n-1 and cur_c == m-1:
                return cur_effort
            
            for dir_r, dir_c in directions:
                new_r, new_c = cur_r + dir_r, cur_c + dir_c

                if 0 <= new_r < n and 0 <= new_c < m:
                    max_effort = max(abs(heights[new_r][new_c] - heights[cur_r][cur_c]), cur_effort)

                    if max_effort < dist[new_r][new_c]:
                        dist[new_r][new_c] = max_effort
                        heappush(pq, (max_effort, new_r, new_c))
        
        return 0
            