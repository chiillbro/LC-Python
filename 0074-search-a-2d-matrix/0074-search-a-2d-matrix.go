func searchMatrix(matrix [][]int, target int) bool {
    n, m := len(matrix), len(matrix[0])

    left, right := 0, n * m -1

    for left <= right {
        mid := (left + right) >> 1

        row, col := mid / m, mid % m

        val := matrix[row][col]

        if val == target {
            return true
        } else if val > target {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }

    return false
}