func canFinish(numCourses int, prerequisites [][]int) bool {
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

    topoCount := 0
    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            cur := queue[0]
            queue = queue[1:]
            topoCount++

            for _, pre := range adj_list[cur] {
                inDegree[pre]--

                if inDegree[pre] == 0 {
                    queue = append(queue, pre)
                }
            }
        }
    }

    return topoCount == numCourses

}