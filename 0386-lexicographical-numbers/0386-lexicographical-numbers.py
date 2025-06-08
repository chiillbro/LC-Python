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

        # res = []


        # def dfs(cur):
        #     if cur > n:
        #         return
            
        #     res.append(cur)

        #     for i in range(10):
        #         next_num = cur * 10 + i

        #         if next_num > n:
        #             break
        #         dfs(next_num)


        # for i in range(1, 10):
        #     if i > n:
        #         break
        #     dfs(i)

        # return res