/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    // if p == nil && q == nil {
    //     return true
    // }

    // if p == nil || q == nil {
    //     return false
    // }

    type Pair struct {
        node1, node2 *TreeNode
    }
    stack := make([]Pair, 0)

    stack = append(stack, Pair{p, q})

    for len(stack) > 0 {
        nodes := stack[len(stack)-1]

        node1, node2 := nodes.node1, nodes.node2
        
        stack = stack[:len(stack)-1]
        if node1 == nil && node2 == nil {
            continue
        }

        if node1 == nil || node2 == nil || node1.Val != node2.Val {
            return false
        }

        stack = append(stack, Pair{node1.Left, node2.Left})
        stack = append(stack, Pair{node1.Right, node2.Right})
       
    }

    return len(stack) == 0
}