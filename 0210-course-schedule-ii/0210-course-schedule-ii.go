func findOrder(numCourses int, prerequisites [][]int) []int {
    adj_list := make(map[int][]int, numCourses)

    for _, pair := range prerequisites {
        u, v := pair[1], pair[0]

        adj_list[u] = append(adj_list[u], v)
    }

    inDegree := make([]int, numCourses)

    for _, v := range adj_list {
        for _, crs := range v {
            inDegree[crs]++
        }
    }


    queue := make([]int, 0)

    for crs, v := range inDegree {
        if v == 0 {
            queue = append(queue, crs)
        }
    }

    topo := []int{}

    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]

        topo = append(topo, cur)

        for _, neigh := range adj_list[cur] {
            inDegree[neigh]--
            if inDegree[neigh] == 0 {
                queue = append(queue, neigh)
            }
        }
    }

    if len(topo) != numCourses {
        return []int{}
    }

    return topo
}