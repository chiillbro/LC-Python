class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1, num2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        totalLen = len1 + len2
        idx1, idx2 = (totalLen // 2) - 1, (totalLen // 2)

        i = j = 0

        while i < len1 and j < len2:
            cnt = i + j
            if nums1[i] < nums2[j]:
                if cnt == idx1:
                    num1 = nums1[i]
                elif cnt == idx2:
                    num2 = nums1[i]
                i += 1
            else:
                if cnt == idx1:
                    num1 = nums2[j]
                elif cnt == idx2:
                    num2 = nums2[j]
                j += 1
            
        while i < len1:
            cnt = i + j
            if cnt == idx1:
                num1 = nums1[i]
            elif cnt == idx2:
                num2 = nums1[i]
            i += 1
        while j < len2:
            cnt = i + j
            if cnt == idx1:
                num1 = nums2[j]
            elif cnt == idx2:
                num2 = nums2[j]
            j += 1

        if (totalLen & 1) == 0:
            return (num1 + num2) / 2.0
        else:
            return float(num2)
            