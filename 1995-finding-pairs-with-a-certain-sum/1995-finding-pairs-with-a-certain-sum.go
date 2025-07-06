type FindSumPairs struct {
    nums2Map map[int]int
    // updatedIndices map[int]int
    nums1 []int
    nums2 []int
}


func Constructor(nums1 []int, nums2 []int) FindSumPairs {
    nums2Map := make(map[int]int, len(nums2))
    // updatedIndices := make(map[int]int, len(nums2))

    for _, v := range nums2 {
        // nums1Map[v] = append(nums1Map[v], i)
        nums2Map[v]++
    }

    return FindSumPairs{
        nums2Map,
        // updatedIndices,
        nums1,
        nums2,
    }
}


func (this *FindSumPairs) Add(index int, val int)  {
    this.nums2Map[this.nums2[index]]--
    this.nums2[index] += val
    this.nums2Map[this.nums2[index]]++
}


func (this *FindSumPairs) Count(tot int) int {
    count := 0

    for _, v := range this.nums1 {
        compliment := tot - v
        if cnt, exists := this.nums2Map[compliment]; exists {
            count += cnt
        }
    }

    return count
}


/**
 * Your FindSumPairs object will be instantiated and called as such:
 * obj := Constructor(nums1, nums2);
 * obj.Add(index,val);
 * param_2 := obj.Count(tot);
 */