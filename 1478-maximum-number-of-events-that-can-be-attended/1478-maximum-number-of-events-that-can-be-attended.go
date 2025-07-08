import (
    "sort"
    "container/heap"
)

type MinHeap []int

func (h MinHeap) Len() int { return len(h) }

func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }

func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(val interface{}) {
    *h = append(*h, val.(int))
}

func (h *MinHeap) Pop() interface{} {
    old := *h

    n := len(old)

    x := old[n-1]

    *h = old[:n-1]

    return x
}


func maxEvents(events [][]int) int {
    sort.Slice(events, func (i, j int) bool { return events[i][0] < events[j][0]} )

    maxDay := 0

    for _, event := range events {
        if event[1] > maxDay {
            maxDay = event[1]
        }
    }

    pq := &MinHeap{}

    heap.Init(pq)

    ans, j := 0, 0

    for i := 1; i <= maxDay; i++ {
        for j < len(events) && events[j][0] <= i {
            heap.Push(pq, events[j][1])
            j++
        }

        for pq.Len() > 0 && (*pq)[0] < i {
            heap.Pop(pq)
        }

        if pq.Len() > 0 {
            heap.Pop(pq)
            ans++
        }
    }

    return ans
}