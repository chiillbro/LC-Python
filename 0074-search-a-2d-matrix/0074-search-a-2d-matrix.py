class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid =  (right + left) >> 1
            i, j = mid // n, mid % n
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: right = mid - 1
            else: left = mid + 1
        return False