class Solution:

    def findCount(self, nums: List[int], x: int, v: int) -> int:
        if x > 0:
            return bisect.bisect_right(nums, v // x)
        elif x < 0:
            return len(nums) - bisect.bisect_left(nums, -(-v//x))
        else:
            return len(nums) if v >= 0 else 0


    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)

        left, right = -(10**10), 10**10

        while left <= right:
            mid = (right + left) >> 1

            count = 0

            for i in range(n1):
                count += self.findCount(nums2, nums1[i], mid)
            
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left