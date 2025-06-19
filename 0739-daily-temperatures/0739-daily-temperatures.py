class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        next_warmer_in = [0] * n

        stack = []

        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()


            if not stack:
                next_warmer_in[i] = 0
            else:
                next_warmer_in[i] = abs(stack[-1] - i)
            
            stack.append(i)
        

        return next_warmer_in