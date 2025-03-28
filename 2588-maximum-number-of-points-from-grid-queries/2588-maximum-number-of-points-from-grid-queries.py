class Solution:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])

        # ** Approach one: using min_heap and sorting queries ** #

        # res = [0] * len(queries)
        # visited = [[False] * n for _ in range(m)]
        # heap = []
        # sorted_queries = sorted([(query, i) for i, query in enumerate(queries)])
        # heappush(heap, (grid[0][0], 0, 0))
        # total_points = 0
        # visited[0][0] = True

        # for query, q_idx in sorted_queries:
        #     while heap and heap[0][0] < query:
        #         val, row, col = heappop(heap)
        #         total_points += 1

        #         for dir_r, dir_c in self.directions:
        #             r, c = row + dir_r, col + dir_c
        #             if (0 <= r < m) and (0 <= c < n) and not visited[r][c]:
        #                 heappush(heap, (grid[r][c], r, c))
        #                 visited[r][c] = True
            
        #     res[q_idx] = total_points
        
        # return res


        # ** Approach Two: Using Min Heap and Binary Search ** # (Dijkstra's Algorithm type)
        total_cells = m * n
        total_points_need = [0] * (total_cells + 1)

        min_val_to_reach = [[float('inf')] * n for _ in range(m)]
        min_val_to_reach[0][0] = grid[0][0]
        min_heap = []
        heappush(min_heap, (grid[0][0], 0, 0))
        visited_cells = 0

        while min_heap:
            val, r, c = heappop(min_heap)

            total_points_need[visited_cells + 1] = val
            visited_cells += 1

            for dir_r, dir_c in self.directions:
                row, col = r + dir_r, c + dir_c

                if (0 <= row < m) and (0 <= col < n) and min_val_to_reach[row][col] == float('inf'):
                    min_val_to_reach[row][col] = max(val, grid[row][col])
                    heappush(min_heap, (min_val_to_reach[row][col], row, col))
        

        res = []
        for query in queries:
            left, right = 0, total_cells

            while left <= right:
                mid = (left + right) >> 1

                if total_points_need[mid] < query:
                    left = mid + 1
                else:
                    right = mid - 1
            
            res.append(right)
        
        return res






# MLE

 # def helper(row, col, i, count):
        #     if not (0 <= row < m) or not (0 <= col < n) or grid[row][col] >= queries[i]:
        #         return count
            
        #     if not (row, col) in visited:
        #         count += 1
        #         visited.add((row, col))
        #     # DOWN
        #     count += helper(row + 1, col, i, count)
        #     # UP
        #     count += helper(row - 1, col, i, count)
        #     # LEFT
        #     count += helper(row, col - 1, i, count)
        #     # RIGHT
        #     count += helper(row, col + 1, i, count)

        #     return count

        
        # for i in range(len(queries)):
        #     res.append(helper(0, 0, i, 0))


