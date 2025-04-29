class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return sum(nums)

        start = n - k
        length = k << 1
        left = 0
        res = current_sum = 0

        for right in range(length):
            current_sum += nums[(start + right) % n]
            while right - left + 1 > k:
                current_sum -= nums[(left + start) % n]
                left += 1

            res = max(res, current_sum)
        
        return res
