// var cycleStart int = -1

type DSU struct {
    parent []int
    rank []int
}

func UnionFind (n int) *DSU {
    parent := make([]int, n)

    for i := range n {
        parent[i] = i
    }

    rank := make([]int, n)

    for i := range n {
        rank[i] = 1
    }

    return &DSU{
        parent, rank,
    }
}

func (uf *DSU) find(x int) int {
    if uf.parent[x] != x {
        uf.parent[x] = uf.find(uf.parent[x])
    }

    return uf.parent[x]
}

func (uf *DSU) union(x, y int) bool {
    xRoot, yRoot := uf.find(x), uf.find(y)

    if xRoot == yRoot {
        return false
    }

    if uf.rank[xRoot] < uf.rank[yRoot] {
        xRoot, yRoot = yRoot, xRoot
    }

    uf.parent[yRoot] = xRoot
    uf.rank[xRoot] += uf.rank[yRoot]

    return true
}

func findRedundantConnection(edges [][]int) []int {
    N := len(edges)

    // adjList := make(map[int][]int)

    uf := UnionFind(N)

    for _, edge := range edges {
        u, v := edge[0]-1, edge[1]-1

        if !uf.union(u, v) {
            return edge
        }
    }

    return []int{}


    // Approach 1: DFS (Brute)
    // for _, edge := range edges {
    //     visited := make([]bool, N)

    //     if isConnected(edge[0]-1, edge[1]-1, visited, adjList) {
    //         return edge
    //     }

    //     adjList[edge[0]-1] = append(adjList[edge[0]-1], edge[1]-1)
    //     adjList[edge[1]-1] = append(adjList[edge[1]-1], edge[0]-1)
    // }

    // return []int{}

    // for _, edge := range edges {
    //     u, v := edge[0]-1, edge[1]-1
    //     adjList[u] = append(adjList[u], v)

    //     adjList[v] = append(adjList[v], u)
    // }

    // parent := make([]int, N)

    // for i := range N {
    //     parent[i] = -1
    // }

    // visited := make([]bool, N)

    // var dfs func (cur int)

    // dfs = func (src int) {
    //     visited[src] = true

    //     for _, neigh := range adjList[src] {
    //         if !visited[neigh] {
    //              parent[neigh] = src
    //              dfs(neigh)
    //         } else if neigh != parent[src] && cycleStart == -1 {
    //             cycleStart = neigh
    //             parent[neigh] = src
    //         }
    //     }
    // }

    // dfs(0)

    // cycleNodes := make(map[int]struct{})

    // node := cycleStart
    // for {
    //     cycleNodes[node] = struct{}{}
    //     node = parent[node]
    //     if node == cycleStart {
    //         break
    //     }
    // }

    // for i := N-1; i >= 0; i-- {
    //     edge := edges[i]

    //     // if cycleNodes[edge[0]-1] != nil && cycleNodes[edge[1]-1] != nil {
    //     //     return edge
    //     // }

    //     _, exists := cycleNodes[edge[0]-1]
    //     _, ok := cycleNodes[edge[1]-1]

    //     if exists && ok {
    //         return edge
    //     }
    // }

    // return []int{}

}


// func isConnected(src, parent int, visited []bool, adjList map[int][]int) bool {
//     visited[src] = true

//     if src == parent {
//         return true
//     }

//     isFound := false

//     for _, neigh := range adjList[src] {
//         if !visited[neigh] {
//             isFound = isFound || isConnected(neigh, parent, visited, adjList)
//         }
//     }


//     return isFound
// }