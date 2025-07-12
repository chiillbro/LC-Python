/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    
    if root == nil {
        return [][]int{}
    }
    res := make([][]int, 0)

    queue := make([]*TreeNode, 0)
    queue = append(queue, root)

    for len(queue) > 0 {
        level := make([]int, 0)

        size := len(queue)

        for i := 0; i < size; i++ {
            cur := queue[0]
            queue = queue[1:]

            level = append(level, cur.Val)

            if cur.Left != nil {
                queue = append(queue, cur.Left)
            }

            if cur.Right != nil {
                queue = append(queue, cur.Right)
            }
        }

        res = append(res, level)
    }

    return res
}