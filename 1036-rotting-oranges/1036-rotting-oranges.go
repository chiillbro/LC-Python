var dirs = [4][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func orangesRotting(grid [][]int) int {
    n, m := len(grid), len(grid[0])

    grid_copy := make([][]int, n)

    copy(grid_copy, grid)

    queue := make([][2]int, 0, n*m)

    fresh := 0
    for r := range n {
        for c := range m {
            switch grid[r][c] {
                case 2:
                    queue = append(queue, [2]int{r, c})
                case 1:
                    fresh++
            }
        }
    }

    minutes := 0
    for len(queue) > 0 && fresh > 0 {
        length := len(queue)
        for i := 0; i < length; i++ {
            cur := queue[0]
            queue = queue[1:]

            for _, dir := range dirs {
                new_r, new_c := cur[0] + dir[0], cur[1] + dir[1]

                if min(new_r, new_c) < 0 || new_r >= n  || new_c >= m || grid_copy[new_r][new_c] != 1 {
                    continue
                }

                fresh--
                grid_copy[new_r][new_c] = 2
                queue = append(queue, [2]int{new_r, new_c})
            }

        }


        minutes++
    }

    if fresh > 0 {
        return -1
    }

    return minutes


}