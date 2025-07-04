func dailyTemperatures(temperatures []int) []int {
    n := len(temperatures)
    res := make([]int , n)

    stack := make([]int , 0, n)

    for i, v := range temperatures {
        for len(stack) > 0 && v > temperatures[stack[len(stack)-1]] {
            top := stack[len(stack) - 1]

            res[top] = i - top

            stack = stack[:len(stack)-1]
        }

        stack = append(stack, i)
    }

    return res
}