func search(nums []int, target int) int {
    n := len(nums)

    left, right := 0, n-1

    for left <= right {
        mid := (left + right) >> 1

        if nums[mid] == target {
            return mid
        }

        if nums[left] <= nums[mid] {
            if nums[left] <= target && nums[mid] > target {
                right = mid - 1
            } else {
                left = mid + 1
            }
        } else {
            if nums[right] >= target && nums[mid] < target {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
    }

    return -1
}