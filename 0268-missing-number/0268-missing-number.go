func missingNumber(nums []int) int {
    n := len(nums)
    sumShouldBe := (n * (n + 1)) >> 1

    actualSum := 0

    for _, num := range nums {
        actualSum += num
    }

    return sumShouldBe - actualSum

}