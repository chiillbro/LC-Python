class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        res = ""

        lower_threshold, upper_threshold = -2 ** 31, 2 ** 31 - 1

        for i, char in enumerate(s):
            if res and not char.isdigit():
                break
            
            if not res and char not in ('+', '-') and not char.isdigit():
                break

            res += char
        
        if not res or (len(res) == 1 and not res.isdigit()):
            return 0

        if lower_threshold <= int(res) <= upper_threshold:
            return int(res)
        elif int(res) < lower_threshold:
            return lower_threshold
        else:
            return upper_threshold