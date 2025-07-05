func findRedundantConnection(edges [][]int) []int {
    N := len(edges)

    adjList := make(map[int][]int)

    for _, edge := range edges {
        visited := make([]bool, N)

        if isConnected(edge[0]-1, edge[1]-1, visited, adjList) {
            return edge
        }

        adjList[edge[0]-1] = append(adjList[edge[0]-1], edge[1]-1)
        adjList[edge[1]-1] = append(adjList[edge[1]-1], edge[0]-1)
    }

    return []int{}

    // for _, edge := range edges {
    //     u, v := edge[0], edge[1]
    //     adjList[u] = append(adjList[u], v)

    //     adjList[v] = append(adjList[v], u)
    // }

    // visited := make([]bool, n+1)

    // var dfs func (cur, parent int)

    // dfs = func (cur, parent int) {
    //     visited[cur] = true

    //     for _, neigh := range adjList[cur] {
    //         if !visited[neigh] {
    //             if 
    //         }
    //     }
    // }



    // return dfs(1, -1)



}


func isConnected(src, parent int, visited []bool, adjList map[int][]int) bool {
    visited[src] = true

    if src == parent {
        return true
    }

    isFound := false

    for _, neigh := range adjList[src] {
        if !visited[neigh] {
            isFound = isFound || isConnected(neigh, parent, visited, adjList)
        }
    }


    return isFound
}