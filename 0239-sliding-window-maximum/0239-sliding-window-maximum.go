func maxSlidingWindow(nums []int, k int) []int {
    n := len(nums)

    res := make([]int, 0, n - k + 1)

    queue := list.New()

    for i := 0; i < n; i++ {
        if queue.Len() > 0 && queue.Front().Value.(int) < i - k + 1 {
            queue.Remove(queue.Front())
        }

        for queue.Len() > 0  && nums[queue.Back().Value.(int)] < nums[i] {
            queue.Remove(queue.Back())
        }

        queue.PushBack(i)

        if i >= k - 1 {
            res = append(res, nums[queue.Front().Value.(int)])
        }

    }

    return res
}