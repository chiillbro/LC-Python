import (
    "math"
)

type Pair struct {
    time int
    node int
}

type MinHeap []*Pair

func (h MinHeap) Len() int { return len(h) }

func (h MinHeap) Less(i, j int) bool { return h[i].time < h[j].time}

func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
    *h = append(*h, x.(*Pair))
}

func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)

    x := old[n-1]

    *h = old[:n-1]

    return x
}

func networkDelayTime(times [][]int, n int, k int) int {

    type neiPair struct {
        nei int
        w int
    }
    adjList := make(map[int][]neiPair, n)

    for _, edge := range times {
        u, v, w := edge[0], edge[1], edge[2]
        adjList[u] = append(adjList[u], neiPair{v, w})
    }

    dist := make([]int, n+1)

    for i := range n+1 {
        if i == k {
            continue
        }
        dist[i] = math.MaxInt32
    }

    h := &MinHeap{}

    heap.Init(h)

    heap.Push(h, &Pair{0, k})

    for h.Len() > 0 {
        cur := heap.Pop(h).(*Pair)

        if cur.time > dist[cur.node] {
            continue
        }
        for _, nei := range adjList[cur.node] {
            if newDelay := cur.time + nei.w; newDelay < dist[nei.nei] {
                dist[nei.nei] = newDelay
                heap.Push(h, &Pair{newDelay, nei.nei})
            }
        }
    }

    maxDelay := 0

    for i := 1; i <= n; i++ {
        if dist[i] == math.MaxInt32 {
            return -1
        }
        maxDelay = max(maxDelay, dist[i])
    }

    return maxDelay
}