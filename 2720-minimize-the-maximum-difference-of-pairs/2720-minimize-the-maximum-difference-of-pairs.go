import (
    "sort"
)

func minimizeMax(nums []int, p int) int {
    n := len(nums)

    sort.Ints(nums)

    left, right := 0, nums[n - 1] - nums[0]

    var countPairs = func(target int) int {
        i, count := 0, 0

        for i < n - 1 {
            if nums[i+1] - nums[i] <= target {
                count++
                i++
            }
            i++
        }

        return count
    }

    for left <= right {
        mid := (left + right) >> 1

        if countPairs(mid) >= p {
            right = mid - 1
        } else {
            left = mid + 1
        }

    } 

    return left

}