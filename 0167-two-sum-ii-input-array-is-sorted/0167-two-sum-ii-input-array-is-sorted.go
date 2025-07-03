func twoSum(numbers []int, target int) []int {
    n := len(numbers)

    l, r := 0, n-1

    res := make([]int, 2)
    for l < r {
        if cur := numbers[l] + numbers[r]; cur == target {
            res[0], res[1] = l+1, r+1
            break
        } else if cur > target {
            r--
        } else {
            l++
        }
    }

    return res
}