/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    
    // Floyd's Tortoise and hare cycle detection algorithm

    tortoise, hare := head, head

    for hare != nil && hare.Next != nil {
        tortoise = tortoise.Next
        hare = hare.Next.Next

        if tortoise == hare {
            return true
        }
    }

    return false
}