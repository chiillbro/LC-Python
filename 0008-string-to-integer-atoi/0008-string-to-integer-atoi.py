class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        lower_threshold, upper_threshold = -2 ** 31, 2 ** 31 - 1

        i, n = 0, len(s)
        sign = 1

        res = 0

        if s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i = 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if res > (upper_threshold - digit) // 10:
                return upper_threshold if sign == 1 else lower_threshold
            else:
                res = res * 10 + digit
            
            i += 1
        
        return max(lower_threshold, min(sign * res, upper_threshold))