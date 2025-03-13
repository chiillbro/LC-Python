class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)

        def canDivide(k):
            _sum = 0
            for num in nums:
                _sum += math.ceil(num/k)
                if _sum > threshold: return False
            
            return _sum <= threshold

        ans = -1
        while low <= high:
            mid = low + (high - low) // 2

            if canDivide(mid): 
                ans = mid
                high = mid - 1
            else: low = mid + 1
        
        return ans
