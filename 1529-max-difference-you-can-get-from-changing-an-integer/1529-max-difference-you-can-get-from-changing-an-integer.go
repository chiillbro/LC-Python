import "fmt"

func maxDiff(num int) int {
    sNum := strconv.Itoa(num)

    val_a := num

    replace := func(x, y string) string {
		return strings.ReplaceAll(sNum, x, y)
	}

    for _, char := range sNum {
        fmt.Println("char", char)
        if char != '9' {
            val_a, _ = strconv.Atoi(replace(string(char), "9"))
            break
        }
    }

    // fmt.Println("val_a", val_a)


    val_b := num

    // fmt.Println("sNum", sNum)
    for i, char := range sNum {
        if i == 0 {
            if char != '1' {
                val_b, _ = strconv.Atoi(replace(string(char), "1"))
                break
            }
        } else {
            if char != '0' && char != '1' {
                val_b, _ = strconv.Atoi(replace(string(char), "0"))
                break
            }
        }
    }

    return val_a - val_b
}