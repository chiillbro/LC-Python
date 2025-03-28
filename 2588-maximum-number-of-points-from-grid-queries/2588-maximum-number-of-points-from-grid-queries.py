class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        m, n = len(grid), len(grid[0])
        visited = set()
        heap = []
        sorted_queries = sorted([(query, i) for i, query in enumerate(queries)])
        heappush(heap, (grid[0][0], 0, 0))
        total_points = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited.add((0, 0))

        for query, q_idx in sorted_queries:
            while heap and heap[0][0] < query:
                val, row, col = heappop(heap)
                total_points += 1

                for dir_r, dir_c in directions:
                    r, c = row + dir_r, col + dir_c
                    if (0 <= r < m) and (0 <= c < n) and (r, c) not in visited:
                        heappush(heap, (grid[r][c], r, c))
                        visited.add((r, c))
            
            res[q_idx] = total_points
        
        return res



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


