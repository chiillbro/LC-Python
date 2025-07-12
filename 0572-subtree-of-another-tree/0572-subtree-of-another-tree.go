/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
    if subRoot == nil {
        return true
    }

    if root == nil {
        return false
    }

    if isIdentical(root, subRoot) {
        return true
    }

    return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)

}

func isIdentical(node1, node2 *TreeNode) bool {
    if node1 == nil && node2 == nil {
        return true
    }

    if node1 == nil || node2 == nil || node1.Val != node2.Val {
        return false
    }

    return isIdentical(node1.Left, node2.Left) && isIdentical(node1.Right, node2.Right)
}