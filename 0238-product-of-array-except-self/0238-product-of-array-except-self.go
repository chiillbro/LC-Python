func productExceptSelf(nums []int) []int {

    n := len(nums)

    mulLeft := make([]int, n)

    mulLeft[0] = nums[0]

    for i := 1; i < n; i++ {
        mulLeft[i] = mulLeft[i-1] * nums[i]
    }

    mulRight := make([]int, n)

    mulRight[n-1] = nums[n-1]

    for i := n-2; i >= 0; i-- {
        mulRight[i] = mulRight[i+1] * nums[i]
    }

    res := make([]int, n)

    res[0] = mulRight[1]

    res[n-1] = mulLeft[n-2]

    for i := 1; i < n-1; i++ {
        res[i] = mulLeft[i-1] * mulRight[i+1]
    }

    return res
}