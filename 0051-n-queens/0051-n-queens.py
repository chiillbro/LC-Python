class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def backtrack(col, board):
            if col == n:
                res.append([''.join(board[i]) for i in range(n)])
            
            for row in range(n):
                if self.isSafe(row, col, board, n):
                    board[row][col] = 'Q'
                    backtrack(col + 1, board)
                    board[row][col] = '.'

        
        board = [['.' for _ in range(n)] for _ in range(n)]
        # for r in range(n):
        #     board[r][0] = 'Q'
        #     backtrack(, set((r, 0)))
        #     board[r][0] = '.'
        backtrack(0, board)

        return res

    def isSafe(self, row, col, board, n):
        if col == 0:
            return True
        
        if 'Q' in board[row]:
            return False
        
        tempRow, tempCol = row - 1, col - 1

        while tempRow >= 0 and tempCol >= 0:
            if board[tempRow][tempCol] == 'Q':
                return False
            tempRow -= 1
            tempCol -= 1
        

        tempRow, tempCol = row + 1, col - 1

        while tempRow < n and tempCol >= 0:
            if board[tempRow][tempCol] == 'Q':
                return False
            tempRow += 1
            tempCol -= 1
        
        return True
