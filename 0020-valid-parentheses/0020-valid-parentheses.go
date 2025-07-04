func isValid(s string) bool {
    n := len(s)

    stack := make([]rune, 0, n)

    for _, r := range s {
        if r == '(' || r == '[' || r == '{' {
            stack = append(stack, r)
        } else {
            if len(stack) > 0 {
                switch r {
                    case ')':
                        if stack[len(stack)-1] != '(' {
                            return false
                        }
                    case ']':
                        if stack[len(stack)-1] != '[' {
                            return false
                        }
                    case '}':
                        if stack[len(stack)-1] != '{' {
                            return false
                        }

                }
                stack = stack[:len(stack) - 1]
            } else {
                return false
            }
        }
    }

    if len(stack) > 0 {
        return false
    }

    return true
}