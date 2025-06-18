func nextGreaterElements(nums []int) []int {
    n := len(nums)

    stack := []int{}

    res := make([]int, n)

    for i := range n {
        res[i] = -1
    }

    for i := n * 2; i >= 0; i-- {
        idx := i % n

        for len(stack) != 0 && stack[len(stack)-1] <= nums[idx] {
            stack = stack[:len(stack)-1]
        }

        if len(stack) != 0 {
            res[idx] = stack[len(stack) - 1]
        }

        stack = append(stack, nums[idx])
    }

    return res
}