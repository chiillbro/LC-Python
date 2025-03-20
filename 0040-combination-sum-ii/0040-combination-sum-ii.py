class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def calculateSum(curRem, i, sol):
            if curRem == 0:
                res.append(sol[:])
                return
            elif i == n: return

            for j in range(i, n):
                cur = candidates[j]
                if cur > curRem:
                    break
                if j > i and cur == candidates[j-1]: continue
                sol.append(cur)
                calculateSum(curRem - cur, j + 1, sol)
                sol.pop()
        
        calculateSum(target, 0, [])
        return res
