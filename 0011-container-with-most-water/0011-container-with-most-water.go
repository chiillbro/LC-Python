func maxArea(height []int) int {

    n := len(height)
    area := 0

    left, right := 0, n-1

    for left < right {
        width := right - left

        hei := min(height[left], height[right])

        curArea := width * hei

        area = max(curArea, area)

        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }

    return area
}