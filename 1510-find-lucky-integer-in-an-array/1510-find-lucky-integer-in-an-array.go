func findLucky(arr []int) int {
    freq := make(map[int]int, len(arr))

    for _, v := range arr {
        freq[v]++
    }

    luckyInt := -1
    for k, v := range freq {
        if k == v {
            luckyInt = max(luckyInt, k)
        }
    }

    return luckyInt
}