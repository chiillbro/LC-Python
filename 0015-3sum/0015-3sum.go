import (
    "sort"
)
func threeSum(nums []int) [][]int {

    sort.Slice(nums, func (i, j int) bool { return nums[i] < nums[j] })

    n := len(nums)

    res := [][]int{}

    for i := 0; i < n-2; i++ {
        if i > 0  && nums[i] == nums[i-1] {
            continue
        }
        left, right := i + 1, n - 1

        for left < right {
            curSum := nums[i] + nums[left] + nums[right]

            if curSum == 0 {
                res = append(res, []int{nums[i], nums[left], nums[right]})

                for left < right && nums[left] == nums[left+1] {
                    left++
                }

                for left < right && nums[right] == nums[right-1] {
                    right--
                }

                left++
                right--
            } else if curSum < 0 {
                left++
            } else {
                right--
            }
        }
    }

    return res
}