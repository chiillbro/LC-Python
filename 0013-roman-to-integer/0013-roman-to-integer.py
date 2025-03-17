class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = prev = 0

        for char in reversed(s):
            cur_val = roman_to_int[char]

            if cur_val < prev:
                total -= cur_val
            else:
                total += cur_val

            prev = cur_val
        
        return total