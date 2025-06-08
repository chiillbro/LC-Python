class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        cur = 1

        for _ in range(n):
            res.append(cur)

            if cur * 10 <= n:
                cur *= 10
            
            else:
                if cur >= n:
                    cur //= 10
                
                cur += 1

                while not (cur % 10):
                    cur //= 10
        
        return res