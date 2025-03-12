class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]

        low, high = 1, N - 2

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid & 1 == 0:
                if nums[mid] == nums[mid + 1]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid] == nums[mid + 1]:
                    high = mid - 1
                else:
                    low = mid + 1