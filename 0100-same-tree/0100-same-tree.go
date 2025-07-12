/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p == nil && q == nil {
        return true
    }

    if p == nil || q == nil {
        return false
    }
    stack1 := []*TreeNode{p}

    stack2 := []*TreeNode{q}

    for len(stack1) > 0  && len(stack2) > 0 {
        cur1, cur2 := stack1[len(stack1)-1], stack2[len(stack2)-1]
        
        stack1 = stack1[:len(stack1)-1]
        stack2 = stack2[:len(stack2)-1]

        if cur1.Val != cur2.Val {
            return false
        }

        if cur1.Left != nil && cur2.Left == nil {
            return false
        } else if cur1.Left == nil && cur2.Left != nil {
            return false
        } else if cur1.Left != nil && cur2.Left != nil {
            stack1 = append(stack1, cur1.Left)
            stack2 = append(stack2, cur2.Left)
        }

        if cur1.Right != nil && cur2.Right == nil {
            return false
        } else if cur1.Right == nil && cur2.Right != nil {
            return false
        } else if cur1.Right != nil && cur2.Right != nil {
            stack1 = append(stack1, cur1.Right)
            stack2 = append(stack2, cur2.Right)
        }
    }

    return len(stack1) == 0 && len(stack2) == 0
}