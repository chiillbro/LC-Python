/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummyNode := &ListNode{}

    cur := dummyNode

    l1, l2 := list1, list2

    for l1 != nil && l2 != nil {
        val := min(l1.Val, l2.Val)
        newNode := &ListNode{val, nil}

        if l1.Val == val {
            l1 = l1.Next
        } else {
            l2 = l2.Next
        }

        cur.Next = newNode

        cur = newNode
    }

    for l1 != nil {
        newNode := &ListNode{l1.Val, nil}

        l1 = l1.Next
        
        cur.Next = newNode
        cur = newNode
    }

    for l2 != nil {
        newNode := &ListNode{l2.Val, nil}

        l2 = l2.Next
        
        cur.Next = newNode
        cur = newNode
    }

    return dummyNode.Next
}