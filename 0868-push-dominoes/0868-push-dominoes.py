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


        symbols = [(i, c) for i, c in enumerate(dominoes) if c != '.']

        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)

        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:
                for k in range(i+1, j):
                    ans[k] = '.LR'[self.cmp(k-i, j-k)]
        
        return ''.join(ans)
    

    def cmp(self, a, b):
        return (a > b) - (a < b)