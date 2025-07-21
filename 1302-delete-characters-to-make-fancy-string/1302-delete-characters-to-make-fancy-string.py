class Solution:
    def makeFancyString(self, s: str) -> str:
        if not s: return ""

        res = [s[0]]

        cnt = 1

        for cur in s[1:]:
            prev = res[-1]
            if cur == prev:
                cnt += 1
            else:
                cnt = 1
            
            if cnt < 3:
                res.append(cur)
        
        return ''.join(res)

