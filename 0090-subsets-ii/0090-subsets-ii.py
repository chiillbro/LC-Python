class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        def backtrack(i : int, sol : List[int]):
            if i == n:
                res.add(tuple(sol))
                return
            
            backtrack(i + 1, sol)
            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()
        
        backtrack(0, [])

        return [list(t) for t in res]

        # for mask in range(1 << n):
        #     subset = []

        #     for i in range(n):
        #         if mask & (1 << i):
        #             subset.append(nums[i])
        #     res.add(tuple(subset))
        # return [list(t) for t in res]

        