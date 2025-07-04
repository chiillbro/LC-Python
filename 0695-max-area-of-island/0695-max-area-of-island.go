var dirs = [4][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func maxAreaOfIsland(grid [][]int) int {
    n, m := len(grid), len(grid[0])

    visited := make([][]bool, n)

    for i := range n {
        visited[i] = make([]bool, m)
    }

    var bfs func (row, col int) int

    bfs = func (r, c int) int {
        visited[r][c] = true

        dq := make([][]int, 0, n*m)

        dq = append(dq, []int{r, c})

        cur := 0
        for len(dq) > 0 {
            pair := dq[0]
            dq = dq[1:]

            cur++

            for _, curDir := range dirs {
                newRow, newCol := pair[0] + curDir[0], pair[1] + curDir[1]

                if newRow >= 0 && newRow < n && newCol >= 0 && newCol < m && grid[newRow][newCol] != 0 && !visited[newRow][newCol] {
                    visited[newRow][newCol] = true
                    dq = append(dq, []int{newRow, newCol})
                }
            }
        }

        return cur

    }
    
    // var dfs func (row, col int) int

    // dfs = func (r, c int) int {
    //     if !(r >= 0 && r < n && c >= 0 && c < m) || visited[r][c] || grid[r][c] == 0 {
    //         return 0
    //     }

    //     visited[r][c] = true

    //     cur := 1
    //     cur += dfs(r-1, c) + dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1)

    //     return cur
    // }

    maxArea := 0
    for r := range n {
        for c := range m {
            if grid[r][c] == 0 || visited[r][c] {
                continue
            }

            maxArea = max(maxArea, bfs(r, c))
        }
    }

    return maxArea
}