class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def calculateSum(curRem, i, sol):
            if curRem == 0:
                res.append(sol[:])
                return
            elif i == n: return
            # if i == n:
            #     if curRem == 0:
            #         res.append(sol[:])
            #     return
            
            if candidates[i] <= curRem:
                sol.append(candidates[i])
                calculateSum(curRem - candidates[i], i, sol)
                sol.pop()
            

            # if curRem  == 0:
            #     res.append(sol[:])
            #     return
            # elif i == n or curRem < 0:
            #     return
            # sol.append(candidates[i])
            # calculateSum(curRem - candidates[i], i, sol)
            # sol.pop()
            calculateSum(curRem, i + 1, sol)
        
        calculateSum(target, 0, [])
        return res