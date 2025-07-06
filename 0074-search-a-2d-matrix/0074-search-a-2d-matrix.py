class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        left, right = 0, n*m - 1


        while left <= right:
            mid = (left + right) >> 1

            row, col = mid // m, mid%m

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
        # left, right = 0, len(matrix) - 1

        # while left <= right:
        #     mid = (left + right) >> 1

        #     if matrix[mid][0] == target:
        #         return True
        #     elif matrix[mid][0] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # row  = right
        # left, right = 0, len(matrix[0]) - 1

        # while left <= right:
        #     mid = (left + right) >> 1

        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return False