class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # n = len(dominoes)
        # stack = []
        # for i, c in enumerate(dominoes):
        #     if c == '.':
        #         if not stack:
        #             if i + 1 <= n - 1 and dominoes[i+1] == 'L':
        #                 stack.append('L')
        #             else:
        #                 stack.append(c)
        #         else:
        #             if i == n - 1:
        #                 if stack[-1] == 'R':
        #                     stack.append('R')
        #                 else:
        #                     stack.append(c)
        #             else:
        #                 if stack[-1] == 'R' and dominoes[i+1] == 'L':
        #                     stack.append(c)
        #                 elif stack[-1] == 'L' and dominoes[i+1] == 'R':
        #                     stack.append(c)
        #                 elif stack[-1] == 'L' and dominoes[i+1] == 'L':
        #                     stack.append('L')
        #                 else:
        #                     stack.append('R')
        #     else:
        #         stack.append(c)
        
        # return ''.join(stack)


    #     symbols = [(i, c) for i, c in enumerate(dominoes) if c != '.']

    #     symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

    #     ans = list(dominoes)

    #     for (i, x), (j, y) in zip(symbols, symbols[1:]):
    #         if x == y:
    #             for k in range(i+1, j):
    #                 ans[k] = x
    #         elif x > y:
    #             for k in range(i+1, j):
    #                 ans[k] = '.LR'[self.cmp(k-i, j-k)]
        
    #     return ''.join(ans)


        N = len(dominoes)

        force = [0] * N

        f = 0

        for i, c in enumerate(dominoes):
            if c == 'R':
                f = N
            elif c == 'L':
                f = 0
            else: f = max(f-1, 0)

            force[i] += f

        f = 0
        for i in range(N-1, -1, -1):
            c = dominoes[i]
            if c == 'R':
                f = 0
            elif c == 'L':
                f = N
            else: f = max(f-1, 0)

            force[i] -= f
        
        return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in force)

    

    def cmp(self, a, b):
        return (a > b) - (a < b)