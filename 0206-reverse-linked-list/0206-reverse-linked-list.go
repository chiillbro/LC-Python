/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    // dummyNode := &ListNode{}

    // dummyNode.Next = head

    var prev *ListNode

    cur := head

    for cur != nil {
        nxt := cur.Next

        cur.Next = prev
        prev = cur
        cur = nxt
    }

    return prev
}