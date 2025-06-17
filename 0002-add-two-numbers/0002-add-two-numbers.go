/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummyNode := &ListNode{}

    p := l1
    q := l2
    cur := dummyNode

    carry := 0

    for p != nil || q != nil || carry != 0 {
        val1 := 0
        if p != nil {
            val1 = p.Val
            p = p.Next
        }
        val2 := 0

        if q != nil {
            val2 = q.Val
            q = q.Next
        }

        cur_sum := val1 + val2 + carry

        carry = cur_sum / 10

        cur.Next = &ListNode{cur_sum % 10, nil}
        cur = cur.Next
        
    }

    return dummyNode.Next
}