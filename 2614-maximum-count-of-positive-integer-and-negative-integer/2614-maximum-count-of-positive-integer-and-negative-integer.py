class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        N = len(nums)
        # l, r = 0, N - 1
        # pos = neg = res = 0

        # while l < r:
        #     if nums[l] < 0:
        #         neg += 1
        #     elif nums[l] > 0:
        #         pos += 1
            
        #     if nums[r] < 0:
        #         neg += 1
        #     elif nums[r] > 0:
        #         pos += 1
            
        #     l += 1
        #     r -= 1
        
        # return max(pos, neg)

        # ** Follow up - using Binary Search **

        low, high = 0, N - 1
        lower_bound, upper_bound = N, N

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= 0:
                lower_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        
        # if lower_bound == 0 and nums[lower_bound - 1] != 0:
        #     return N
        
        low, high = 0, N - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] > 0:
                upper_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return max(lower_bound, N - upper_bound)