var dirs = [4][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func solve(board [][]byte)  {
    n, m := len(board), len(board[0])

    visited := make(map[[2]int]bool)

    var bfs func(row, col int)

    bfs = func(row, col int) {
        coord := [2]int{row, col}
        visited[coord] = true

        queue := [][2]int{{row, col}}

        for len(queue) > 0 {
            cur := queue[0]

            queue = queue[1:]

            for _, dir := range dirs {
                new_r, new_c := cur[0] + dir[0], cur[1] + dir[1]
                newCoord := [2]int{new_r, new_c}
                if min(new_r, new_c) < 0 || new_r >= n || new_c >= m || visited[newCoord] || board[new_r][new_c] != 'O' {
                    continue
                }

                visited[newCoord] = true
                queue = append(queue, newCoord)
            }
        }
    }


    for r := range n {
        for c := range m {
            if (r == 0 || c == 0 || r == n-1 || c == m-1) && board[r][c] == 'O' {
                bfs(r, c)
            }
        }
    }

    for r := range n {
        for c := range m {
            coord := [2]int{r, c}
            if board[r][c] == 'O' && !visited[coord] {
                board[r][c] = 'X'
            }
        }
    }
}