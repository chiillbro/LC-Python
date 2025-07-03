import (
    "unicode"
    "strings"
)

func isPalindrome(s string) bool {
    f := func (r rune) rune {
        if !unicode.IsLetter(r) && !unicode.IsNumber(r) {
            return -1
        }

        return unicode.ToLower(r)
    }


    s = strings.Map(f, s)

    l, r := 0, len(s) - 1
    for l < r {
        if s[l] != s[r] {
            return false
        }

        l++
        r--
    }

    return true
}