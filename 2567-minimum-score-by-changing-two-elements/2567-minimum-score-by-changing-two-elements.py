class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        sorted_nums = sorted(nums)
        
        two_smallest_changed = sorted_nums[-1] - sorted_nums[2]
        two_greatest_changed = sorted_nums[-3] - sorted_nums[0]
        one_each_changed = sorted_nums[-2] - sorted_nums[1]
        
        return min(two_smallest_changed, two_greatest_changed, one_each_changed)