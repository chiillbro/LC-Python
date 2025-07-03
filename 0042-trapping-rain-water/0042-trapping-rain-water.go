func trap(height []int) int {

    n := len(height)
    trapped := 0

    left, right := 1, n-2

    leftMax, rightMax := height[0], height[n-1]

    for left <= right {
        if leftMax <= rightMax {
            if height[left] < leftMax {
                trapped += leftMax - height[left]
            } else {
                leftMax = height[left]
            }

            left++
        } else {
            if height[right] < rightMax {
                trapped += rightMax - height[right]
            } else {
                rightMax = height[right]
            }
            right--
        }
    }


    return trapped

}