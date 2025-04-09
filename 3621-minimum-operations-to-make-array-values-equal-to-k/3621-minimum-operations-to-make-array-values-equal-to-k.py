class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        if min(nums_set) < k:
            return -1
        
        if k in nums_set:
            return len(nums_set) - 1
        return len(nums_set)