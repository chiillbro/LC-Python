class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        low, high = 0, N - 1

        while low <= high:
            mid = low + (high - low) // 2

            if mid & 1 == 0:
                if mid < N - 1 and nums[mid] == nums[mid + 1]:
                    low = mid + 1
                elif mid > 0 and nums[mid] == nums[mid - 1]:
                    high = mid - 1
                else:
                    return nums[mid]
            else:
                if mid < N - 1 and nums[mid] == nums[mid + 1]:
                    high = mid - 1
                elif mid > 0 and nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    return nums[mid]