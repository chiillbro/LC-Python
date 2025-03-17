class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) >> 1
            
            max_el = (-1, -1)

            for i in range(m):
                if mat[i][mid] > max_el[1]:
                    max_el = (i, mat[i][mid])
            row, val = max_el
            if (mid == 0 or mat[row][mid - 1] < val) and (mid == n - 1 or mat[row][mid + 1] < val):
                return [row, mid]
            elif mid > 0 and mat[row][mid - 1] > val:
                high = mid - 1
            else:
                low = mid + 1
            

