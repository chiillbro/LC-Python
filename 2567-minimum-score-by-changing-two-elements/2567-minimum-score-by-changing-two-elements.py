class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # sorted_nums = sorted(nums) # O(n log n)
        
        # two_smallest_changed = sorted_nums[-1] - sorted_nums[2]
        # two_greatest_changed = sorted_nums[-3] - sorted_nums[0]
        # one_each_changed = sorted_nums[-2] - sorted_nums[1]


        # O(n log 3) ~ O(n)
        three_smallest = nsmallest(3, nums)
        three_largest = nlargest(3, nums)

        two_smallest_changed = three_largest[0] - three_smallest[2]
        two_greatest_changed = three_largest[-1] - three_smallest[0]
        one_each_changed = three_largest[1] - three_smallest[1]
        
        return min(two_smallest_changed, two_greatest_changed, one_each_changed)