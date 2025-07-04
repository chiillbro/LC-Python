func largestRectangleArea(heights []int) int {
    n := len(heights)
    stack := make([]struct{idx, height int}, 0, n)

    maxArea := 0

    for i, h := range heights {
        start := i
        for len(stack) > 0 && stack[len(stack)-1].height > h {
            cur := stack[len(stack)-1]
            stack = stack[:len(stack)-1]

            maxArea = max(maxArea, cur.height * (i - cur.idx))
            start = cur.idx
        }
        
        stack = append(stack, struct{idx, height int}{start, h})
    }

    for _, cur := range stack {
        maxArea = max(maxArea, cur.height * (n - cur.idx))
    }

    return maxArea
}