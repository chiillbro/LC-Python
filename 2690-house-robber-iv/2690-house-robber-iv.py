class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)

        def canRobWithCapacity(capacity):
            robbed, i = 0, 0

            while i < N and robbed <= k:
                if nums[i] <= capacity:
                    robbed += 1
                    i += 1
                i += 1
            
            return robbed >= k


        low, high = min(nums), max(nums)

        while low <= high:
            mid = (high + low) >> 1
            
            if canRobWithCapacity(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
