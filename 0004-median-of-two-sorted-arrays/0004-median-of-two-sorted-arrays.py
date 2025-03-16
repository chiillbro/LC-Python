class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # num1, num2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        N = n1 + n2
        # idx1, idx2 = (N // 2) - 1, (N // 2)

        # i = j = 0

        # ** Approach 1 using two pass : Better Approach **

        # while i < n1 and j < n2:
        #     cnt = i + j
        #     if nums1[i] < nums2[j]:
        #         if cnt == idx1:
        #             num1 = nums1[i]
        #         elif cnt == idx2:
        #             num2 = nums1[i]
        #         i += 1
        #     else:
        #         if cnt == idx1:
        #             num1 = nums2[j]
        #         elif cnt == idx2:
        #             num2 = nums2[j]
        #         j += 1
        
        # if num1 and num2:
        #     if (N & 1) == 0:
        #         return (num1 + num2) / 2.0
        #     else:
        #         return float(num2)
            
        # while i < n1:
        #     cnt = i + j
        #     if cnt == idx1:
        #         num1 = nums1[i]
        #     elif cnt == idx2:
        #         num2 = nums1[i]
        #     i += 1
        # while j < n2:
        #     cnt = i + j
        #     if cnt == idx1:
        #         num1 = nums2[j]
        #     elif cnt == idx2:
        #         num2 = nums2[j]
        #     j += 1

        # if (N & 1) == 0:
        #     return (num1 + num2) / 2.0
        # else:
        #     return float(num2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, n1
        elements = (N + 1) // 2

        while low <= high:
            mid1 = (low + high) >> 1
            mid2 = elements - mid1
            l1 = l2 = float("-inf")
            r1 = r2 = float("inf")

            if mid1 < n1: r1 = nums1[mid1]
            if mid2 < n2: r2 = nums2[mid2]

            if mid1 > 0: l1 = nums1[mid1 - 1]
            if mid2 > 0: l2 = nums2[mid2 - 1]

            if l1 <= r2 and l2 <= r1:
                if N & 1 == 0:
                    return (min(r1, r2) + max(l1, l2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2: high = mid1 - 1
            else: low = mid1 + 1


            