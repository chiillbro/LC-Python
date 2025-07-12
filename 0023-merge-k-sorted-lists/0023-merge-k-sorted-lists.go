/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type HeapElement struct {
    val, idx int
    node *ListNode
}

type MinHeap []*HeapElement

func (pq MinHeap) Len() int { return len(pq) }

func (pq MinHeap) Less(i, j int) bool {
    if pq[i].val < pq[j].val {
        return true
    } else if pq[i].val > pq[j].val {
        return false
    }
    
    return pq[i].idx < pq[j].idx
}  

func (pq MinHeap) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *MinHeap) Push(element interface{}) {
    *pq = append(*pq, element.(*HeapElement))
}

func (pq *MinHeap) Pop() interface{} {
    old := *pq

    n := len(old)
    x := old[n-1]

    *pq = old[:n-1]

    return x
}



func mergeKLists(lists []*ListNode) *ListNode {
    k := len(lists)

    pq := &MinHeap{}
    heap.Init(pq)

    for i := 0; i < k; i++ {
        if lists[i] != nil {
            heap.Push(pq, &HeapElement{lists[i].Val, i, lists[i]})
        }
    }

    dummyHead := &ListNode{0, nil}

    cur := dummyHead

    for pq.Len() > 0 {
        element := heap.Pop(pq).(*HeapElement)

        if element.node.Next != nil {
            heap.Push(pq, &HeapElement{element.node.Next.Val, element.idx, element.node.Next})
        }
        cur.Next = element.node
        cur = cur.Next
    }
    
    return dummyHead.Next
}