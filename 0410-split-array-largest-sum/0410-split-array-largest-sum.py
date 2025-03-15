class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)

        def canSplit(length):
            count, curSum = 1, 0

            for i, v in enumerate(nums):
                if curSum + v <= length:
                    curSum += v
                else:
                    count += 1
                    curSum = v
            
            return count

        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) >> 1

            if canSplit(mid) > k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low