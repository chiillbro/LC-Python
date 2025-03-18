class Solution:
    def myAtoi(self, s: str) -> int:
        # s = s.lstrip()
        # if not s:
        #     return 0

        # threshold = pow(2, 31)

        # i, n = 0, len(s)
        # sign = 1

        # res = 0

        # if s[i] in ('+', '-'):
        #     sign = -1 if s[i] == '-' else 1
        #     i = 1
        
        # while i < n and s[i].isdigit():
        #     digit = int(s[i])

        #     if res > (threshold - 1 - digit) // 10:
        #         return threshold - 1 if sign == 1 else -threshold
        #     else:
        #         res = res * 10 + digit
            
        #     i += 1
        
        # return max(-threshold, min(sign * res, threshold - 1))

        # ** Recursive Solution **

        return self.solve(s.lstrip())

    def solve(self, s : str, ans : str ='') -> int:
        if s and len(ans) == 0 and s[0] in '+-':
            ans += s[0]
            return self.solve(s[1:], ans)
        
        elif s and s[0].isdigit():
            ans += s[0]
            return self.solve(s[1:], ans)
        else:
            ans = 0 if not ans or ans in '+-' else int(ans)

            return max(-2**31, min(ans, 2**31 - 1))
