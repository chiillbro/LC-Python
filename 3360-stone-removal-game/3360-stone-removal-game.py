class Solution:
    def canAliceWin(self, n: int) -> bool:
        # parity = 0
        
        # curr_remove = 10
        # while n >= 1:
        #     if curr_remove > n:
        #         return (parity & 1) != 0
            
        #     n -= curr_remove
        #     curr_remove -= 1
        #     parity += 1
        

        # return (parity & 1) != 0

        parity = 0
        for i in range(10, -1, -1):
            if i <= n:
                n -= i
                parity += 1
            else:
                return (parity & 1) != 0

        
        return (parity & 1) != 0