class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        {1, 2, 0}

        # 1     2   3   4
        # 5     0   7   8
        # 0     10  11  12
        # 13    14  15  0
        n, m = len(matrix), len(matrix[0])
        zero_pos_col = set()
        zero_pos_row = set()

        for row in range(n):
            for col in range(m):
                if not matrix[row][col]:
                    zero_pos_row.add(row)
                    zero_pos_col.add(col)
        
        
        for row in range(n):
            for col in range(m):
                if row in zero_pos_row or col in zero_pos_col and matrix[row][col]:
                    matrix[row][col] = 0
                