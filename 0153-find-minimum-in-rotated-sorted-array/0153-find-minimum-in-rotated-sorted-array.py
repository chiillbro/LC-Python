class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        low, high = 0, N - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]