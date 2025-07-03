func isAnagram(s string, t string) bool {

    if len(s) != len(t) {
        return false
    }

    freq := make([]int, 26)

    for i, char := range s {
        freq[char - 97]++
        freq[t[i] - 97]--
    }

    for _, v := range freq {
        if v != 0 {
            return false
        }
    }

    return true
}