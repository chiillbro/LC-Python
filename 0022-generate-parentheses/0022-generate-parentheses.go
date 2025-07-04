func generateParenthesis(n int) []string {

    var res []string
    
    cur := make([]byte, 0, 2*n)
    
    var backtrack func(openCount, closeCount int)

    backtrack = func (openCount, closeCount int) {
        if openCount == n && closeCount == n {
            res = append(res, string(cur))
            return
        }

        if openCount < n {
            cur = append(cur, '(')
            backtrack(openCount + 1, closeCount)
            cur = cur[:len(cur)- 1]
        }

        if closeCount < openCount {
            cur = append(cur, ')')
            backtrack(openCount, closeCount + 1)
            cur = cur[:len(cur)- 1]
        }
    }

    backtrack(0, 0)

    return res
}