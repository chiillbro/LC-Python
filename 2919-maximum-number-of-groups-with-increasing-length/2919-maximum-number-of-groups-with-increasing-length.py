# class Solution:
#     def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        s = 0
        ans = 0
        for x in usageLimits:
            s += x
            next_group_need = (ans + 1) * (ans + 2) // 2
            if s >= next_group_need:
                ans += 1
        return ans