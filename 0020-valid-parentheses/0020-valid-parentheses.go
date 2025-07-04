func isValid(s string) bool {
    n := len(s)

    pairs := map[rune]rune{
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }

    stack := make([]rune, 0, n)

    for _, r := range s {
        if open, isClose := pairs[r]; isClose {
            if len(stack) == 0 || stack[len(stack)-1] != open {
                return false
            }
            
            stack = stack[:len(stack) - 1]
        } else {
            stack = append(stack, r)
        }
    }

    return len(stack) == 0
}