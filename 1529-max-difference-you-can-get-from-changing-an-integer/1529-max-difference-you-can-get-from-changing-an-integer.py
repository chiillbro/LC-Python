class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)
        n = len(s_num)

        # --- Calculate max_a ---
        # Strategy: Find the first digit from the left that is not '9'.
        # Replace all occurrences of this digit with '9'.
        # If all digits are '9', a is num.
        
        val_a = num
        
        char_for_a_replacement = ''
        for char_digit in s_num:
            if char_digit != '9':
                char_for_a_replacement = char_digit
                break
        if char_for_a_replacement: # Found a non-'9' digit
            val_a = int(s_num.replace(char_for_a_replacement, '9'))


        # --- Calculate min_b ---
        
        val_b = num

        for i, char in enumerate(s_num):
            if not i:
                if char != '1':
                    val_b = int(s_num.replace(char, '1'))
                    break
            else:
                if char != '0' and char != '1':
                    val_b = int(s_num.replace(char, '0'))
                    break
        
        return val_a - val_b