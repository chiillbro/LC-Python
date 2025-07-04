func pacificAtlantic(heights [][]int) [][]int {
    n, m := len(heights), len(heights[0])

    pacific := make(map[[2]int]bool)
    atlantic := make(map[[2]int]bool)

    var dfs func (row, col, parent int, visit map[[2]int]bool)

    dfs = func (row, col, parent int, visit map[[2]int]bool) {
        coord := [2]int{row, col}
        if min(row, col) < 0 || row >= n || col >= m || visit[coord] || heights[row][col] < parent {
            return
        }

        visit[coord] = true

        dfs(row-1, col, heights[row][col], visit)
        dfs(row, col+1, heights[row][col], visit)
        dfs(row+1, col, heights[row][col], visit)
        dfs(row, col-1, heights[row][col], visit)
    }

    for c := range m {
        dfs(0, c, -1, pacific)
        dfs(n-1, c, -1, atlantic)
    }

    for r := range n {
        dfs(r, 0, -1, pacific)
        dfs(r, m-1, -1, atlantic)
    }

    res := make([][]int, 0, n*m)

    for r := range n {
        for c := range m {
            coord := [2]int{r, c}
            if pacific[coord] && atlantic[coord] {
                res = append(res, []int{r, c})
            }
        }
    }

    return res


}