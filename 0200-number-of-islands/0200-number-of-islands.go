// var dirs = [][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

// func numIslands(grid [][]byte) int {
//     n, m := len(grid), len(grid[0])


//     visited := make([][]bool, n)

//     for i := range n {
//         visited[i] = make([]bool, m)
//     }

//     var dfs func (row, col int)

//     dfs = func (row, col int) {
//         if !(row >= 0 && row < n && col >= 0 && col < m) || 
//         grid[row][col] == '0' || 
//         visited[row][col] {
//             return
//         }

//         visited[row][col] = true

//         dfs(row-1, col) // up
//         dfs(row, col+1) // right
//         dfs(row+1, col) // down
//         dfs(row, col-1) // left

//     }

//     islands := 0
//     for r := range n {
//         for c := range m {
//             if grid[r][c] == '0' || visited[r][c] {
//                 continue
//             }
//             dfs(r, c)
//             islands++
//         }
//     }

//     return islands
// }

type UnionFind struct {
    parent []int
    rank []int
    count int
}

func NewUnionFind(grid [][]byte) *UnionFind {
    n, m := len(grid), len(grid[0])
    
    size := n * m

    uf := &UnionFind{
        parent: make([]int, size),
        rank: make([]int, size),
    }

    for i := 0; i < size; i++ {
		uf.parent[i] = -1 // mark all as water by default
	}

    for r := range n {
        for c := range m {

            if grid[r][c] == '1' {
                id := r*m + c
                uf.parent[id] = id
                uf.rank[id] = 0
                uf.count++
            }
        }
    }

    return uf

}

func (uf *UnionFind) find(x int) int {
    if uf.parent[x] != x {
        uf.parent[x] = uf.find(uf.parent[x])
    }

    return uf.parent[x]
}

func (uf *UnionFind) union(x, y int) {
    xRoot, yRoot := uf.find(x), uf.find(y)

    if xRoot == -1 || yRoot == -1 || xRoot == yRoot {
        return
    }

    if uf.rank[xRoot] > uf.rank[yRoot] {
        uf.parent[yRoot] = xRoot
    } else if uf.rank[xRoot] < uf.rank[yRoot] {
        uf.parent[xRoot] = yRoot
    } else {
        uf.parent[yRoot] = xRoot
        uf.rank[xRoot]++
    }

    uf.count--
}

func numIslands(grid [][]byte) int {
    n, m := len(grid), len(grid[0])

    if n == 0 {
		return 0
	}
    uf := NewUnionFind(grid)

    dirs := [][2]int{{0, 1}, {1, 0}}

    for r := range n {
        for c := range m {
            if grid[r][c] != '1' {
                continue
            }

            id := r*m + c

            for _, d := range dirs {
                newR, newC := r + d[0], c + d[1]

                if newR >= 0 && newR < n && newC >= 0 && newC < m && grid[newR][newC] == '1' {
                    newId := newR*m + newC
                    uf.union(id, newId)
                }
            }
        }
    }

    return uf.count
}