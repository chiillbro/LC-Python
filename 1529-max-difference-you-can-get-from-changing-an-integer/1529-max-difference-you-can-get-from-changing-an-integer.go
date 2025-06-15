import "fmt"

func maxDiff(num int) int {
    sNum := strconv.Itoa(num)

    val_a := num

    for _, char := range sNum {
        fmt.Println("char", char)
        if char != '9' {
            valToConvert := strings.ReplaceAll(sNum, string(char), "9")
            fmt.Println("valToConvert", valToConvert)
            val_a, _ = strconv.Atoi(valToConvert)
            fmt.Println("val_a", val_a)
            break
        }
    }

    fmt.Println("val_a", val_a)


    val_b := num

    fmt.Println("sNum", sNum)
    for i, char := range sNum {
        if i == 0 {
            if char != '1' {
                valToConvert := strings.ReplaceAll(sNum, string(char), "1")
                val_b, _ = strconv.Atoi(valToConvert)
                break
            }
        } else {
            if char != '0' && char != '1' {
                valToConvert := strings.ReplaceAll(sNum, string(char), "0")
                val_b, _ = strconv.Atoi(valToConvert)
                break
            }
        }
    }

    return val_a - val_b
}