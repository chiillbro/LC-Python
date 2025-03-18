class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)

        # ** First Approach using Binary Search on answers **
    #     result = 1
        
    #     low, high = 0, len(nums)

    #     while low <= high:
    #         mid = (low + high) >> 1

    #         if self._can_form_nice_subarray(nums, mid):
    #             result = mid
    #             low = mid + 1
    #         else:
    #             high = mid - 1
        
    #     return result

        # ** Second Method using Sliding window **

        start = used_bits = max_length = 0

        for end in range(N):
            while used_bits & nums[end] != 0:
                used_bits ^= nums[start]
                start += 1
            
            used_bits |= nums[end]

            max_length = max(max_length, end - start + 1)
        
        return max_length

    def _can_form_nice_subarray(self, nums, length):
        if length <= 1: return True

        for start in range(len(nums) - length + 1):
            is_nice = True
            bit_mask = 0

            for pos in range(start, start + length):
                if bit_mask & nums[pos] != 0:
                    is_nice = False
                    break
                bit_mask |= nums[pos]
            
            if is_nice:
                return True
        return False



