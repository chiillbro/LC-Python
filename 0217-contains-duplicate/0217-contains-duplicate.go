func containsDuplicate(nums []int) bool {
    seen := make(map[int]int, len(nums))

    for i, num := range nums {
        if _, ok := seen[num]; ok {
            return true
        }

        seen[num] = i
    }

    return false
}