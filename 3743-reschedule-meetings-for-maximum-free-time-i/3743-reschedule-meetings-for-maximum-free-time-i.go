func maxFreeTime(eventTime int, k int, startTime []int, endTime []int) int {
    n := len(startTime)

    gaps := make([]int, 0, n+1)

    gaps = append(gaps, startTime[0] - 0)

    for i := 0; i < n-1; i++ {
        gaps = append(gaps, startTime[i + 1] - endTime[i])
    }

    gaps = append(gaps, eventTime - endTime[n-1])

    windowSize := k + 1 // for k moves, the total no.of gaps contributed = +1

    if len(gaps) <= windowSize {
        return Sum(gaps)
    }

    currentWindowSum := Sum(gaps[:windowSize])
    maxFreeTime := currentWindowSum

    for i := 1; i <= len(gaps) - windowSize; i++ {
        currentWindowSum = currentWindowSum  - gaps[i-1] + gaps[i + windowSize - 1]

        maxFreeTime = max(maxFreeTime, currentWindowSum)
    }

    return maxFreeTime

}

func Sum (nums []int) int {
    totalSum := 0

    for _, num := range nums {
        totalSum += num
    }

    return totalSum
}