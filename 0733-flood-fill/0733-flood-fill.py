class Solution:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if color == original:
            return image

        m, n = len(image), len(image[0])

        # ** DFS Approach ** #

        def dfs(row: int, col: int) -> None:
            if (0 <= row < m) and (0 <= col < n) and image[row][col] == original:
                image[row][col] = color

                for dir_r, dir_c in self.directions:
                    dfs(dir_r + row, dir_c + col) 

        # ** BFS Approach ** #
        # queue = deque([(sr, sc)])

        # while queue:
        #     for _ in range(len(queue)):
        #         r, c = queue.popleft()
        #         image[r][c] = color

        #         for dir_r, dir_c in self.directions:
        #             row, col = r + dir_r, c + dir_c
        #             if (0 <= row < m) and (0 <= col < n) and image[row][col] == original:
        #                 queue.append((row, col))
        
        dfs(sr, sc)
        return image
