/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummyNode := &ListNode{}

    p1, p2 := l1, l2
    cur := dummyNode

    carry := 0

    for p1 != nil || p2 != nil || carry != 0 {
        val1 := 0

        if p1 != nil {
            val1 = p1.Val
            p1 = p1.Next
        }

        val2 := 0

        if p2 != nil {
            val2 = p2.Val
            p2 = p2.Next
        }


        curVal := val1 + val2 + carry


        carry = curVal / 10

        newNode := &ListNode{curVal % 10, nil}

        cur.Next = newNode
        cur = cur.Next
    }

    return dummyNode.Next
}