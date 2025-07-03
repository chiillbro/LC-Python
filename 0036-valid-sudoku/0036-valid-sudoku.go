func isValidSudoku(board [][]byte) bool {
    var rows, cols, boxes [9][10]bool

    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            b := board[i][j]

            d := b - '0' // converting ascii to digit

            if d < 1 || d > 9 {
                continue
            }
            
            boxIndex := (i / 3) * 3 + j / 3

            if rows[i][d] || cols[j][d] || boxes[boxIndex][d] {
                return false
            }

            rows[i][d] = true
            cols[j][d] = true
            boxes[boxIndex][d] = true

        }
    }

    return true
}