class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = l + (r - l) //2
        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid
        
        # minIndex = l
        # if minIndex == 0:
        #     l, r = 0, len(nums) - 1
        # elif target >= nums[0] and target <= nums[minIndex - 1]:
        #     l, r = 0, minIndex - 1
        # else:
        #     l, r = minIndex, len(nums) - 1
        
        # while l <= r:
        #     mid = l + ( r - l ) //2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1 
        