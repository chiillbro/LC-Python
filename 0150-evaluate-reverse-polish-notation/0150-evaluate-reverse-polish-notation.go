import (
    "strconv"
)

func evalRPN(tokens []string) int {
    n := len(tokens)
    stack := make([]int, 0, n)

    for _, s := range tokens {
        if s == "+" || s == "-" || s == "*" || s == "/" {
            num1, num2 := stack[len(stack)-2], stack[len(stack)-1]
            stack = stack[:len(stack)-2]

            fmt.Println("applyOp, num1, num2, op", num1, num2, s, applyOp(num1, num2, s))
            stack = append(stack, applyOp(num1, num2, s))

        } else {
            num, _ := strconv.Atoi(s)
            stack = append(stack, num)
        }
    }

    return stack[0]

}

func applyOp(num1, num2 int, operation string) int {

    switch operation {
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        default:
            return -1
    }
}