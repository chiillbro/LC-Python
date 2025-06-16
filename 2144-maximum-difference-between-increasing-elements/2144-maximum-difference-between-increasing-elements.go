func maximumDifference(nums []int) int {
    n := len(nums)

    prevMin := nums[0]

    ans := -1

    for i := 1; i < n; i++ {
        if nums[i] > prevMin {
            ans = max(ans, nums[i] - prevMin)
        } else {
            prevMin = nums[i]
        }
    }

    return ans
}