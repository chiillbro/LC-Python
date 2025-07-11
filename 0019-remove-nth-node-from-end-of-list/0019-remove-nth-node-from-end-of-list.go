/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummyNode := &ListNode{}

    dummyNode.Next = head

    ahead, behind := head, dummyNode

    for i := 0; i < n; i++ {
        ahead = ahead.Next
    }

    for ahead != nil {
        ahead = ahead.Next
        behind = behind.Next
    }

    behind.Next = behind.Next.Next

    return dummyNode.Next
}