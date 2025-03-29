class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        queue = deque([(sr, sc)])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        original = image[sr][sc]
        if color == original:
            return image

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                image[r][c] = color

                for dir_r, dir_c in directions:
                    row, col = r + dir_r, c + dir_c
                    if (0 <= row < m) and (0 <= col < n) and image[row][col] == original:
                        queue.append((row, col))
        
        return image


        