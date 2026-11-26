class Solution:
    def canAliceWin(self, n: int) -> bool:
        removed_times = 0
        
        curr_remove = 10
        while n >= 1:
            if curr_remove > n:
                return (removed_times & 1) != 0
            
            n -= curr_remove
            curr_remove -= 1
            removed_times += 1
        

        return (removed_times & 1) != 0