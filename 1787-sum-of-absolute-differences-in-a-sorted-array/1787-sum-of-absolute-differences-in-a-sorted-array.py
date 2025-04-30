class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_sum = [nums[0]]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            prefix_sum.append(prefix_sum[-1] + num)
        
        res = []

        for i, num in enumerate(nums):
            left_sum = prefix_sum[i] - num
            right_sum = prefix_sum[-1] - prefix_sum[i]

            left_count = i
            right_count = n - 1 - i

            left_total = left_count * num - left_sum
            right_total = right_sum - right_count * num
            
            res.append(left_total + right_total)
        
        return res
