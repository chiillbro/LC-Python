func isAnagram(s string, t string) bool {
    freq := make([]int, 26)

    for _, char := range s {
        freq[char - 97]++
    }

    for _, char := range t {
        freq[char-97]--
    }

    for _, v := range freq {
        if v != 0 {
            return false
        }
    }

    return true
}