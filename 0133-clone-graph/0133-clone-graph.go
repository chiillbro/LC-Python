/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {

    if node == nil {
        return nil
    }
    clonedNode := &Node{Val :node.Val, Neighbors : []*Node{}}

    visited := make(map[*Node]*Node)

    visited[node] = clonedNode

    dq := []*Node{node}

    for len(dq) > 0 {
        curNode := dq[0]
        dq = dq[1:]

        for _, neigh := range curNode.Neighbors {
            if _, exists := visited[neigh]; !exists {
                clonedNeigh := &Node{neigh.Val, []*Node{}}
                visited[neigh] = clonedNeigh
                dq = append(dq, neigh)
            }

            visited[curNode].Neighbors = append(visited[curNode].Neighbors, visited[neigh])
        }
    }

    return clonedNode
}