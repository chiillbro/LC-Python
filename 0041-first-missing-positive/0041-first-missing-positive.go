func firstMissingPositive(nums []int) int {

    // Most optimal and clever approach

    n := len(nums)
    for i := range n {
        for 1 <= nums[i] && nums[i] <= n && nums[nums[i]-1] != nums[i] {
            correctIdx := nums[i] - 1

            nums[correctIdx], nums[i] = nums[i], nums[correctIdx]
        }
    }


    for i := range n {
        if nums[i] != i + 1 {
            return i + 1
        }
    }

    return n + 1

    // numsSet := make(map[int]struct{}, len(nums))

    // for _, num := range nums {
    //     numsSet[num] = struct{}{}
    // }

    // for i := range len(nums) + 2 {
    //     if i == 0 {
    //         continue
    //     }
    //     if _, exists := numsSet[i]; !exists {
    //         return i
    //     }
    // }

    // return -1

}