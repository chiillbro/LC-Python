class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0

        seen = [0] * (max(nums) + 1)

        n = len(nums)

        for i in range(n):
            if res >= n - i: break
            
            odd = even = 0
            for j in range(i, n):
                val = nums[j]

                if seen[val] != i + 1:
                    seen[val] = i + 1

                    if val & 1: odd += 1
                    else: even += 1
                if odd == even:
                    res = max(res, j - i + 1)
        

        return res
