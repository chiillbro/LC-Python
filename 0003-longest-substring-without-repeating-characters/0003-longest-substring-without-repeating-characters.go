func lengthOfLongestSubstring(s string) int {
    // classic sliding window problem

    // Golang doesn't support set/hashset, so I need to make use of map to mock the set functionality

    runes := []rune(s)
    lastIndex := make(map[rune]int, len(runes))

    left := 0
    maxLen := 0

    for right, char := range runes {
        if prevIdx, seen := lastIndex[char]; seen && prevIdx >= left {
            left = prevIdx + 1 
        }

        lastIndex[char] = right

        if cur := right - left + 1; cur > maxLen {
            maxLen = cur
        }
    }

    return maxLen
}


func Max(a, b int) int {
    if a > b {
        return a
    }

    return b
}