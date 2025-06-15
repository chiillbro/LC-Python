class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)
        n = len(s_num)

        # --- Calculate max_a ---
        # Strategy: Find the first digit from the left that is not '9'.
        # Replace all occurrences of this digit with '9'.
        # If all digits are '9', a is num.
        
        val_a = num # Default if no change or all '9's
        # Iterate through all digits 'x' that could be replaced
        for digit_x_to_replace_char in "0123456789":
            if digit_x_to_replace_char not in s_num:
                continue
            
            # Replace digit_x with '9'
            temp_s_a = s_num.replace(digit_x_to_replace_char, '9')
            # No validation needed for 'a' regarding leading zeros or becoming 0,
            # as replacing with '9' won't cause that if original num >= 1.
            val_a = max(val_a, int(temp_s_a))
        
        # A more direct way for max_a:
        char_for_a_replacement = ''
        for char_digit in s_num:
            if char_digit != '9':
                char_for_a_replacement = char_digit
                break
        if char_for_a_replacement: # Found a non-'9' digit
            val_a = int(s_num.replace(char_for_a_replacement, '9'))
        else: # All digits were '9'
            val_a = num


        # --- Calculate min_b ---
        # Strategy: Try all (digit_x_to_replace, digit_y_to_replace_with) combinations.
        # Ensure the resulting number is valid (no leading zero if len > 1, not zero).
        
        val_b = num # Default if no beneficial change can be made
                      # (or if num is already the smallest possible after one op)

        # Iterate through all possible digits 'x' (0-9) present in num_s
        for char_x_val_to_replace in "0123456789":
            if char_x_val_to_replace not in s_num:
                continue

            # Iterate through all possible digits 'y' (0-9) to replace 'x' with
            for char_y_replacement_digit in "0123456789":
                
                # Perform the replacement: replace all char_x_val_to_replace with char_y_replacement_digit
                # Need to do this carefully if char_x and char_y are part of a multi-digit number string
                
                # Simpler: use string replace
                transformed_s_b = s_num.replace(char_x_val_to_replace, char_y_replacement_digit)

                # Validate: No leading zeros (if length > 1)
                if len(transformed_s_b) > 1 and transformed_s_b[0] == '0':
                    continue 

                current_b_candidate = int(transformed_s_b)

                # Validate: Not zero
                if current_b_candidate == 0:
                    continue
                
                val_b = min(val_b, current_b_candidate)
        
        return val_a - val_b