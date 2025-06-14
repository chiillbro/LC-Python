func minMaxDifference(num int) int {
    numStr := strconv.Itoa(num)

    temp := numStr

    var to_map byte
    for i := 0; i < len(numStr); i++ {
        if numStr[i] != '9' {
            to_map = numStr[i]
            break
        }
    }

    _max := num

    if to_map != 0 {
        _max, _ = strconv.Atoi(strings.ReplaceAll(numStr, string(to_map), "9"))
    }

    first := temp[0]
    _min, _ := strconv.Atoi(strings.ReplaceAll(temp, string(first), "0"))

    return _max - _min
}