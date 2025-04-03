class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        # ** Approach One: Using Dijkstra's algorithm ** TC: (n^2 log n^2)#

        # dist = [[float("inf")] * n for _ in range(n)]
        # dist[0][0] = 1
        # heap = [(1, 0, 0)]

        # while heap:
        #     distance, cur_row, cur_col = heappop(heap)
        #     if new_r == n-1 and new_c == n-1:
        #         return distance
            
        #     for dr, dc in directions:
        #         new_r, new_c = cur_row + dr, cur_col + dc

        #         if (0 <= new_r < n) and (0 <= new_c < n) and not grid[new_r][new_c]:
        #             if distance + 1 < dist[new_r][new_c]:
        #                 dist[new_r][new_c] = distance + 1
        #                 heappush(heap, (distance + 1, new_r, new_c))
        

        # return dist[n-1][n-1] if dist[n-1][n-1] != float("inf") else -1



        # ** There is no need of using Dijkstra's algorithm for solving this problem, because the given graph is uniformly weighted or unweighted, so we can just use standard BFS to find the shortest path to the corner node and the TC also improves significantly which will be O(n^2)

        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0, 1)])
        visited[0][0] = True

        while queue:
            cur_r, cur_c, distance = queue.popleft()

            if cur_r == n-1 and cur_c == n-1:
                return distance
            
            for dr, dc in directions:
                r, c = cur_r + dr, cur_c + dc

                if (0 <= r < n) and (0 <= c < n) and not visited[r][c] and not grid[r][c]:
                    visited[r][c] = True
                    queue.append((r, c, distance + 1))
        
        return -1
