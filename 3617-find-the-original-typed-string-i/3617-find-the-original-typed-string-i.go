func possibleStringCount(word string) int {
    runes := []rune(word)
    // counts := make(map[rune]int, len(runes))

    // for _, r := range runes {
    //     counts[r] += 1
    // }

    // res := 1
    // for _, v := range counts {
    //     if v > 1 {
    //         res  += v - 1
    //     }
    // }

    // return res

    n := len(runes)
    res := 1

    i := 0
    for i < n {
        j := i + 1
        for j < n && runes[i] == runes[j] {
            j++
        }

        if j - i > 1 {
            res += j - i - 1
        }

        i = j
    }

    return res
}