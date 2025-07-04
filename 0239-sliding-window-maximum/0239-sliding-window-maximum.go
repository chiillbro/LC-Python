func maxSlidingWindow(nums []int, k int) []int {
    n := len(nums)

    res := make([]int, 0, n - k + 1)

    // deque := list.New()

    deque := make([]int, 0, n)

    for i := 0; i < n; i++ {
        // if deque.Len() > 0 && deque.Front().Value.(int) < i - k + 1 {
        //     deque.Remove(deque.Front())
        // }

        if len(deque) > 0  && deque[0] <= i - k {
            deque = deque[1:]
        }

        // for deque.Len() > 0  && nums[deque.Back().Value.(int)] < nums[i] {
        //     deque.Remove(deque.Back())
        // }

        for len(deque) > 0 && nums[deque[len(deque)-1]] < nums[i] {
            deque = deque[:len(deque)-1]
        }

        // deque.PushBack(i)
        deque = append(deque, i)

        if i >= k - 1 {
            // res = append(res, nums[deque.Front().Value.(int)])
            res = append(res, nums[deque[0]])
        }

    }

    return res
}