func minWindow(s string, t string) string {

    if len(t) > len(s) {
        return ""
    }

    n, m := len(s), len(t)

    var freqT, freqWindow [128]int

    for i := 0; i < m; i++ {
        freqT[t[i]]++
    }

    required := 0

    for _, v := range freqT {
        if v > 0 {
            required++
        }
    }

    left, formed := 0, 0
    start, minLength := 0, n + 1

    for right := 0; right < n; right++ {
        c := s[right]
        freqWindow[c]++

        if freqT[c] == freqWindow[c] {
            formed++
        }

        for left <= right && formed == required {
            if length := right - left + 1; length < minLength {
                start = left
                minLength = length
            }
            
            c := s[left]
            freqWindow[c]--
            
            if freqWindow[c] < freqT[c] {
                formed--
            }

            left++
        }
    }

    if minLength > n {
        return ""
    }

    return s[start:start+minLength]
}