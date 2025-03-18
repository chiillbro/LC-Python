class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        # ** Approach one : using Backtracking **
        # def backtrack(i):
        #     if i == n:
        #         res.append(sol.copy())
        #         return
        #     backtrack(i + 1)

        #     sol.append(nums[i])
        #     backtrack(i + 1)
        #     sol.pop()
        
        # backtrack(0)

        ## Approach two : Using Bit Manipulation

        for mask in range(1 << n):
            subset = []

            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            res.append(subset)
        return res