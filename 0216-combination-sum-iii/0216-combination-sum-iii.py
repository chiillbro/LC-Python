class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        res = []

        def calculateSum(curRem, i, cnt, sol):
            if cnt == k and curRem == 0:
                res.append(sol[:])
                return
            elif i == 9:
                return
            
            if nums[i] <= curRem and cnt < k:
                sol.append(nums[i])
                calculateSum(curRem - nums[i], i + 1, cnt + 1, sol)
                sol.pop()
                calculateSum(curRem, i + 1, cnt, sol)
            
        calculateSum(n, 0, 0, [])
        return res