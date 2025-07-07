func firstMissingPositive(nums []int) int {
    numsSet := make(map[int]struct{}, len(nums))

    for _, num := range nums {
        numsSet[num] = struct{}{}
    }

    for i := range len(nums) + 2 {
        if i == 0 {
            continue
        }
        if _, exists := numsSet[i]; !exists {
            return i
        }
    }

    return -1

}