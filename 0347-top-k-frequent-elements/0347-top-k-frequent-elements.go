type pair struct {
    val int
    freq int
}

type minHeap []pair

func (h minHeap) Len() int { return len(h)}

func (h minHeap) Less(i, j int) bool { return h[i].freq < h[j].freq}

func (h minHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(val interface{}) {
    *h = append(*h, val.(pair))
}

func (h *minHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    old = old[:n-1]

    *h = old

    return x
}

func topKFrequent(nums []int, k int) []int {

    n := len(nums)
    freq := make(map[int]int, n)

    for _, num := range nums {
        freq[num]++
    }

    // buckets := make([][]int, n+1)

    // for k, v := range freq {
    //     buckets[v] = append(buckets[v], k)
    // }

    // res := make([]int, 0, k)

    // for i := n; i >= 0; i-- {
    //     bucket := buckets[i]

    //     for _, v := range bucket {
    //         res = append(res, v)
    //         if len(res) == k {
    //             return res
    //         }
    //     }
    // }

    // return res

    

    // Heap Approach, O(u log k), where u is no.of unique elements, this approach is best when the k is small

    h := &minHeap{}

    heap.Init(h)

    for val, f := range freq {
        heap.Push(h, pair{val, f})

        if h.Len() > k {
            heap.Pop(h)
        }
    }

    res := make([]int, k, k)

    for i := k-1; i >= 0; i-- {
        res[i] = heap.Pop(h).(pair).val
    }


    return res

}