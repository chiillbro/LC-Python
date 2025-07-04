func maxAreaOfIsland(grid [][]int) int {
    n, m := len(grid), len(grid[0])


    visited := make([][]bool, n)

    for i := range n {
        visited[i] = make([]bool, m)
    }
    
    var dfs func (row, col int) int

    dfs = func (r, c int) int {
        if !(r >= 0 && r < n && c >= 0 && c < m) || visited[r][c] || grid[r][c] == 0 {
            return 0
        }

        visited[r][c] = true

        cur := 1
        cur += dfs(r-1, c) + dfs(r, c+1) + dfs(r+1, c) + dfs(r, c-1)

        return cur
    }

    maxArea := 0
    for r := range n {
        for c := range m {
            if grid[r][c] == 0 || visited[r][c] {
                continue
            }

            maxArea = max(maxArea, dfs(r, c))
        }
    }

    return maxArea
}