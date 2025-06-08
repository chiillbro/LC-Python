func lexicalOrder(n int) []int {
    // Pre-allocate slice capacity for efficiency
    res := make([]int, 0, n)

    cur := 1

    for i := 0; i < n; i++ {
        res = append(res, cur)
        
        if cur * 10 <= n {
            cur *= 10
        } else {
            // This condition is if cur has reached n (so its branch is done)
            // OR if cur itself is > n (e.g., cur=2, n=1, then 1 is added, next is 2, 2>1, so 2's branch is invalid)
            // OR if cur's children would exceed n (e.g., cur=1, n=5, then 1*10=10 > 5)
            // The if cur >= n handles cases where cur is n or we are processing a cur
            // that is itself beyond n conceptually (e.g., cur=2 when n=1, after 1 was processed)
            if cur >= n {
                cur /= 10 // Go up one level
            }

            cur += 1 // Try next sibling

            // If cur has become something like 20 (from 19+1), or 10 (from 9+1)
            // or if cur became 0 (from 9 -> 0) and then 1,
            // we need to strip trailing zeros by going up.
            // This also handles the case where cur might become 0 after cur /= 10
            // (e.g., if cur was 1..9 and cur >= n, then cur becomes 0). cur+=1 makes it 1.
            // The while loop then doesn't trigger for cur=1.
            for cur % 10 == 0 {  // Corrected Go "while" loop
                cur /= 10
            }
        }
    }


    return res
}