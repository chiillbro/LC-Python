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
        # zero_pos_col = set()
        # zero_pos_row = set()

        # for row in range(n):
        #     for col in range(m):
        #         if not matrix[row][col]:
        #             zero_pos_row.add(row)
        #             zero_pos_col.add(col)
        
        
        # for row in range(n):
        #     for col in range(m):
        #         if row in zero_pos_row or col in zero_pos_col and matrix[row][col]:
        #             matrix[row][col] = 0
                
        
        # Follow-up -> Constant Space Approach

        is_first_col_zero = False

        for r in range(n):
            if not matrix[r][0]:
                is_first_col_zero = True
            
            for c in range(1, m):
                if not matrix[r][c]:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(n-1, -1, -1):
            for c in range(m-1, 0, -1):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0
            
            if is_first_col_zero:
                matrix[r][0] = 0