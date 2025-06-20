class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # s: string, consists of N, S, E, W
        # k: int

        n = len(s)
        change = k

        ans = 0

        x, y = 0, 0

        for i, char in enumerate(s):
            if char == 'N':
                y += 1
            elif char == 'S':
                y -= 1
            elif char == 'E':
                x += 1
            else:
                x -= 1
            
            ans = max(ans, min(abs(x) + abs(y) + 2 * k, i+1))

        return ans

            
