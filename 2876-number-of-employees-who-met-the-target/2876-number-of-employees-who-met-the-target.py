class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0

        for h in hours:
            if h >= target:
                res += 1
        
        return res