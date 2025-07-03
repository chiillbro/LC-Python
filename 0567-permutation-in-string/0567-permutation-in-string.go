import (
    "fmt"
)

func checkInclusion(s1 string, s2 string) bool {

    if len(s1) > len(s2) {
        return false
    }

    n, m := len(s2), len(s1)

    var track1, track2 [26]int

    for i := 0; i < m; i++ {
        track1[s1[i] - 'a']++
        track2[s2[i] - 'a']++
    }

    matches := 0

    for i := 0; i < 26; i++ {
        if track1[i] == track2[i] {
            matches++
        }
    }

    if matches == 26 {
        return true
    }


    for right := m; right < n; right++ {
        in, out := s2[right] - 'a', s2[right-m] - 'a'

        track2[in]++

        if track1[in] == track2[in] {
            matches++
        } else if track2[in] == track1[in] + 1 {
            matches--
        }

        track2[out]--
        if track1[out] == track2[out] {
            matches++
        } else if track2[out] == track1[out] - 1 {
            matches--
        }

        if matches == 26 {
            return true
        }
        
    }

    return false
}