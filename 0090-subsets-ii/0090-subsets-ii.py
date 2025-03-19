class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def backtrack(start : int, sol : List[int]):
            res.append(sol[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                sol.append(nums[i])
                backtrack(i + 1, sol)
                sol.pop()
        
        backtrack(0, [])
        return res
        # for mask in range(1 << n):
        #     subset = []

        #     for i in range(n):
        #         if mask & (1 << i):
        #             subset.append(nums[i])
        #     res.add(tuple(subset))
        # return [list(t) for t in res]

        