// import (
//     "fmt"
// )

func possibleStringCount(word string) int {
    // runes := []rune("你好你好")

    // fmt.Println("word", word)

    // fmt.Println("runes", runes)
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

    n := len(word)
    res := 1

    i := 0
    for i < n {
        j := i + 1
        for j < n && word[i] == word[j] {
            // fmt.Printf("type of %v is %T\n", word[i], word[i])
            // fmt.Println(word[i], word[j])
            j++
        }

        if j - i > 1 {
            res += j - i - 1
        }

        i = j
    }

    return res
}