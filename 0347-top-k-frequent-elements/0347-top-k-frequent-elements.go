func topKFrequent(nums []int, k int) []int {

    n := len(nums)
    freq := make(map[int]int, n)

    for _, num := range nums {
        freq[num]++
    }

    buckets := make([][]int, n+1)

    for k, v := range freq {
        buckets[v] = append(buckets[v], k)
    }

    res := make([]int, 0, k)

    for i := n; i >= 0; i-- {
        bucket := buckets[i]

        for _, v := range bucket {
            res = append(res, v)
            if len(res) == k {
                return res
            }
        }
    }

    return res
}