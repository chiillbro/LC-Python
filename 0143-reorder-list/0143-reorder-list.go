/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    stack := make([]*ListNode, 0)

    node := head

    for node != nil {
        stack = append(stack, node)
        node = node.Next
    }

    start := head

    cnt := 0
    for cnt < len(stack) - 1 {
        temp := start.Next
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]

        start.Next = node
        node.Next = temp

        start = temp

        cnt++
    }

    start.Next = nil
}