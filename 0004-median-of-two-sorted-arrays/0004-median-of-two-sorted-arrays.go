// const (
//     MaxInt = int(^uint(0) >> 1)
//     MinInt = -MaxInt - 1
// )

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {

    if len(nums1) > len(nums2) {
        return findMedianSortedArrays(nums2, nums1)
    }
    m, n := len(nums1), len(nums2)

    N := n + m

    left, right := 0, m

    elements := (N + 1) >> 1

    for left <= right {
        mid1 := (left + right) >> 1

        mid2 := elements - mid1

        l1, l2 := math.MinInt, math.MinInt
        r1, r2 := math.MaxInt, math.MaxInt

        if mid1 > 0 {
            l1 = nums1[mid1-1]
        }

        if mid2 > 0 {
            l2 = nums2[mid2-1]
        }


        if mid1 < m {
            r1 = nums1[mid1]
        }

        if mid2 < n {
            r2 = nums2[mid2]
        }

        if l1 <= r2 && l2 <= r1 {
            if N & 1 != 0 {
                return float64(max(l1, l2))
            } else {
                return (float64(max(l1, l2)) + float64(min(r1, r2))) / 2.0
            }
        } else if l1 > r2 {
            right = mid1 - 1
        } else {
            left = mid1 + 1
        }
    }
    

    panic("Median cannot be found, please check the input!")
}