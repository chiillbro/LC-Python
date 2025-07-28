class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0

        for num in nums:
            max_or |= num

        res = 0

        def helper(idx, cur_or):
            if cur_or == max_or:
                nonlocal res
                res += 1
            

            for i in range(idx, len(nums)):
                helper(i + 1, cur_or | nums[i])
        
        helper(0, 0)

        return res