func characterReplacement(s string, k int) int {

    n := len(s)
    track := make(map[byte]int, n)

    currentConsider := 0

    left := 0

    maxLength := 0
    for right := 0; right < n; right++ {
        track[s[right]]++

        currentConsider = max(track[s[right]], currentConsider)
        
        if right - left + 1 - currentConsider > k {
            track[s[left]]--
            left++
        }

        maxLength = max(maxLength, right - left + 1)
    }

    return maxLength
}