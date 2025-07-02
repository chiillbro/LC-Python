func twoSum(nums []int, target int) []int {
    look_up := make(map[int]int)

    for i, num := range nums {
        look_up[num] = i
    }


    for i, num := range nums {
        compliment := target - num

        if idx, ok := look_up[compliment]; ok && i != idx {
            return []int{idx, i}
        }
    }

    return []int{}
}