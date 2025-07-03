import (
    "unicode/utf8"
)

func isAnagram(s string, t string) bool {

    // if len(s) != len(t) {
    //     return false
    // }

    // freq := [26]int{} // array

    // for i, char := range s {
    //     freq[char - 97]++
    //     freq[t[i] - 97]--
    // }

    // for _, v := range freq {
    //     if v != 0 {
    //         return false
    //     }
    // }

    // return true



    // Follow-up, handling arbitrary unicode, I'll make use of runes as I cannot directly index into
    // a fixed size array

    if utf8.RuneCountInString(s) != utf8.RuneCountInString(t) {
        return false
    }

    freq := make(map[rune]int)

    for _, c := range s {
        freq[c]++
    }

    for _, c := range t {
        freq[c]--

        if freq[c] == 0 {
            delete(freq, c)
        }
    }

    return len(freq) == 0
}