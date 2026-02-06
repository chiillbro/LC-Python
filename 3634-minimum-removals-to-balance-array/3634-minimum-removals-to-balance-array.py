class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        nums.sort()

        right = 0
        ans = n

        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1
            
            ans = min(ans, n - (right - left))
        
        return ans

        # left, right = 0, n - 1

        # while left < right:
        #     mid = (right + left) >> 1

        #     if k * nums[mid] > nums[right]:
        #         return n - right + mid
        #     elif k * nums[left] > nums[mid]:
        #         return mid - left + right - mid
            
        #     if 