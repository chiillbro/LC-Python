/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
    dummyNode := &ListNode{0, head}

    prevGroupEnd := dummyNode

    for {
        curGroupEnd := prevGroupEnd

        for i := 0; i < k; i++ {
            curGroupEnd = curGroupEnd.Next
            if curGroupEnd == nil {
                return dummyNode.Next
            }
        }

        nextGroupStart := curGroupEnd.Next
        curGroupStart := prevGroupEnd.Next

        var prev *ListNode
        cur := curGroupStart

        for cur != nextGroupStart {
            nxt := cur.Next
            cur.Next = prev
            prev = cur
            cur = nxt
        }

        prevGroupEnd.Next = prev

        curGroupStart.Next = nextGroupStart

        prevGroupEnd = curGroupStart
    }

}