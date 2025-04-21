class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        suffix[-1] = nums[-1]
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i] + suffix[i + 1]
        
        res = []

        for i, num in enumerate(nums):
            prefix_sum = 0 if i == 0 else prefix[i - 1]
            suffix_sum = 0 if i == n - 1 else suffix[i + 1]
            cur = ((i * num) - prefix_sum) + (suffix_sum - ((n - i - 1) * num))
            res.append(cur)
        
        return res
        
