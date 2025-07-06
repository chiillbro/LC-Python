import (
    "math"
)

func minEatingSpeed(piles []int, h int) int {

    maxEat := piles[0]
    for _, p := range piles {
        maxEat = max(maxEat, p)
    } 

    left, right := 1, maxEat

    var canEat func (k int) bool

    canEat = func (k int) bool {
        hours := 0

        for _, v := range piles {
            hours += int(math.Ceil(float64(v) / float64(k)))
            if hours > h {
                return false
            }
        }

        return hours <= h
    }
    
    ans := right
    for left <= right {
        mid := (left + right) >> 1

        if canEat(mid) {
            ans = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }

    return ans
}