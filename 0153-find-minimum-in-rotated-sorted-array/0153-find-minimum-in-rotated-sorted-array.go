func findMin(nums []int) int {
    n := len(nums)


    left, right := 0, n - 1

    for left <= right {
        mid := (left + right) >> 1

        if nums[0] <= nums[mid] && nums[n-1] < nums[mid] {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return nums[left]
}