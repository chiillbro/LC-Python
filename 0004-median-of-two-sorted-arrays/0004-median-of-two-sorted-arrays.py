class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        
        left, right = 0, m

        elements_required = (n + m + 1) >> 1 # addition of one to n + m accounts for odd number of elements

        while left <= right:
            mid1 = (left + right) >> 1

            mid2 = elements_required - mid1

            l1 = l2 = -inf
            r1 = r2 = inf

            if mid1 > 0:
                l1 = nums2[mid1-1]
            
            if mid2 > 0:
                l2 = nums1[mid2-1]
            
            if mid1 < m:
                r1 = nums2[mid1]
            
            if mid2 < n:
                r2 = nums1[mid2]
            
            if l1 <= r2 and l2 <= r1:
                if (n + m) & 1:
                    return max(l1, l2) * 1.0
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1