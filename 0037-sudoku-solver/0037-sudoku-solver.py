class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.append((i, j))
                else:
                    mask = 1 << int(board[i][j])

                    rows[i] |= mask
                    cols[j] |= mask
                    box_index = (i // 3) * 3 + (j // 3)
                    boxes[box_index] |= mask
        
        def backtrack(count):
            if count == len(empties):
                return True
            
            i, j = empties[count]
            box_index = (i // 3) * 3 + (j // 3)
            for digit in range(1, 10):
                mask = 1 << digit

                if rows[i] & mask or cols[j] & mask or boxes[box_index] & mask:
                    continue

                board[i][j] = str(digit)
                rows[i] |= mask
                cols[j] |= mask
                boxes[box_index] |= mask

                if backtrack(count + 1):
                    return True

                board[i][j] = '.'
                rows[i] ^= mask
                cols[j] ^= mask
                boxes[box_index] ^= mask

            return False

        backtrack(0)


        # ** Below Recursive Backtracking approach gives TLE ** #
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] == '.':
    #                 for digit in '123456789':
    #                     if self._can_place(board, i, j, digit):
    #                         board[i][j] = digit
    #                         if self.solveSudoku(board):
    #                             return True
    #                         board[i][j] = '.'
    #                 return False
        
    #     return True
    
    # def _can_place(self, board: List[List[str]], row: int, col: int, digit: str) -> bool:
    #     for i in range(9):
    #         if board[row][i] == digit: return False
    #         if board[i][col] == digit: return False

    #         if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == digit:
    #             return False
        
    #     return True
        