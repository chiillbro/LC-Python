class Solution:
    def robotWithString(self, s: str) -> str:
        counts = Counter(s)

        stack = []
        min_char = 'a'
        res = []

        for c in s:
            stack.append(c)
            counts[c] -= 1

            while min_char != 'z' and counts[min_char] == 0:
                min_char = chr(ord(min_char) + 1)
            
            while stack and stack[-1] <= min_char:
                res.append(stack.pop())
        

        return ''.join(res)