class Solution:
    def countAndSay(self, n: int) -> str:
        cur = "1"

        for _ in range(n-1):
            temp, i = [], 0

            while i < len(cur):
                count = 1
                while i < len(cur) - 1 and cur[i] == cur[i+1]:
                    count += 1
                    i += 1
                temp.append(str(count) + cur[i])
                i += 1
            
            cur = ''.join(temp)
        
        return cur


            