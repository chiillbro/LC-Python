class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kandane's Algo (Dynamic Programming Approach)

        res = min_so_far = max_so_far = nums[0]

        for num in nums[1:]:
            temp = min(num, min_so_far * num, max_so_far * num)
            max_so_far = max(num, min_so_far * num, max_so_far * num)

            min_so_far = temp

            res = max(res, max_so_far)
        
        return res