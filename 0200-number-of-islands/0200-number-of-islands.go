// var dirs = [][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func numIslands(grid [][]byte) int {
    n, m := len(grid), len(grid[0])


    visited := make([][]bool, n)

    for i := range n {
        visited[i] = make([]bool, m)
    }

    var dfs func (row, col int)

    dfs = func (row, col int) {
        if !(row >= 0 && row < n && col >= 0 && col < m) || 
        grid[row][col] == '0' || 
        visited[row][col] {
            return
        }

        visited[row][col] = true

        dfs(row-1, col) // up
        dfs(row, col+1) // right
        dfs(row+1, col) // down
        dfs(row, col-1) // left

    }

    islands := 0
    for r := range n {
        for c := range m {
            if grid[r][c] == '0' || visited[r][c] {
                continue
            }
            dfs(r, c)
            islands++
        }
    }

    return islands
}