/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	// if p.Val < root.Val && q.Val < root.Val {
    //     return lowestCommonAncestor(root.Left, p, q)
    // }

    // if p.Val > root.Val && q.Val > root.Val {
    //     return lowestCommonAncestor(root.Right, p, q)
    // }

    // return root

    // Iterative Soluion

    cur := root

    for cur != nil {
        if p.Val < cur.Val && q.Val < cur.Val {
            cur = cur.Left
        } else if p.Val > cur.Val && q.Val > cur.Val {
            cur = cur.Right
        } else {
            return cur
        }
    }

    return nil
}