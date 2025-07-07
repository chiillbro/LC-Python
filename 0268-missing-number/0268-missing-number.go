func missingNumber(nums []int) int {
    // n := len(nums)
    // sumShouldBe := (n * (n + 1)) >> 1

    // actualSum := 0

    // for _, num := range nums {
    //     actualSum += num
    // }

    // return sumShouldBe - actualSum
    


    // Using Bitwise XOR

    xor1, xor2 := 0, 0

    for i, num := range nums {
        xor1 ^= num
        xor2 ^= i + 1
    }

    return xor1 ^ xor2


}