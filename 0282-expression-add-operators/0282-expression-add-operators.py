class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        res = []

        def backtrack(index, prev_operand, cur_operand, value, path):
            if index == N:
                if value == target and not cur_operand:
                    res.append(''.join(path[1:]))
                
                return
            
            cur_operand = cur_operand * 10 + int(num[index])
            str_op = str(cur_operand)

            if cur_operand > 0:
                backtrack(index + 1, prev_operand, cur_operand, value, path)
            

            # Addition

            path.append('+'); path.append(str_op)
            backtrack(index + 1, cur_operand, 0, value + cur_operand, path)
            path.pop(); path.pop()

            # Can substract or multiply only if there are some previous operands
            if path:

                # Substraction
                path.append('-'); path.append(str_op)
                backtrack(index + 1, -cur_operand, 0, value - cur_operand, path)
                path.pop(); path.pop()

                # Multiplication
                path.append('*'); path.append(str_op)
                backtrack(index + 1, cur_operand * prev_operand, 0, value - prev_operand + (cur_operand * prev_operand), path)
                path.pop(); path.pop()
            

        backtrack(0, 0, 0, 0, [])
        return res