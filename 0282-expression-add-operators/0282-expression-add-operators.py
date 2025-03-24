class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        res = []

        def backtrack(index, prev_operand, cur_operand, value, path):
            # Base case: when we have processed all digits.
            if index == N:
                # If the entire string is used and the running value equals the target,
                # also ensure that there is no unfinished operand being built (cur_operand == 0).
                if value == target and not cur_operand:
                    # path[1:] is used to skip the initial operator, if any.
                    res.append(''.join(path[1:]))
                return
            
            # Extend the current operand by including the next digit.
            # Imagine building multi-digit numbers: for "123", first cur_operand is 1,
            # then it becomes 12, then 123.
            cur_operand = cur_operand * 10 + int(num[index])
            str_op = str(cur_operand)  # This is the string representation of the current operand.

            # Important: Prevent operands with multiple digits from starting with '0'.
            # If cur_operand is greater than 0, we can try to extend it (i.e. not inserting any operator yet).
            if cur_operand > 0:
                # This recursive call means: "Do not insert any operator here,
                # keep building the current number." 
                # (For instance, turning "1" into "12" when the next digit is 2.)
                backtrack(index + 1, prev_operand, cur_operand, value, path)

            # Now, we have finished building the current operand.
            # We will now consider inserting an operator before the current operand.
            # When we insert an operator, we "commit" the current operand and reset it to 0.

            # Addition:
            path.append('+')
            path.append(str_op)
            # For addition, we add the current operand to the running total (value).
            # The new prev_operand becomes cur_operand because it's the last operand we just added.
            backtrack(index + 1, cur_operand, 0, value + cur_operand, path)
            path.pop()  # Remove the digit string we appended.
            path.pop()  # Remove the '+' operator.

            # We only try subtraction and multiplication if there's already an operator in the path.
            # This ensures we are not adding an operator at the beginning of the expression.
            if path:
                # Subtraction:
                path.append('-')
                path.append(str_op)
                # For subtraction, we subtract the current operand.
                # The new prev_operand is set to -cur_operand to record the sign.
                backtrack(index + 1, -cur_operand, 0, value - cur_operand, path)
                path.pop()
                path.pop()

                # Multiplication:
                path.append('*')
                path.append(str_op)
                # Multiplication is trickier because of operator precedence.
                # For multiplication, we need to adjust the running value (value) by
                # removing the last operand (prev_operand) and adding the result of multiplying
                # the last operand by the current operand.
                # New prev_operand becomes (prev_operand * cur_operand).
                backtrack(index + 1, cur_operand * prev_operand, 0, value - prev_operand + (cur_operand * prev_operand), path)
                path.pop()
                path.pop()

        # Start the recursion with index 0 and no operands or value.
        backtrack(0, 0, 0, 0, [])
        return res