func longestConsecutive(nums []int) int {

    if len(nums) == 0 {
        return 0
    }

    numsSet := make(map[int]struct{}, len(nums))

    for _, val := range nums {
        numsSet[val] = struct{}{}
    }

    maxLength := 1

    for _, val := range nums {
        if _, hasPrev := numsSet[val-1]; hasPrev { 
            continue
        }
        length := 0
        for x := val; ; x++ {
            if _, hasNext := numsSet[x]; !hasNext {
                break
            } 

            delete(numsSet, x)
            length++
        }

        maxLength = max(maxLength, length)
    }

    return maxLength
}