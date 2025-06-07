class Solution:
    def clearStars(self, s: str) -> str:

        lu = defaultdict(list)
        # lu = [[] for _ in range(26)]
        arr = list(s)

        # has_star = 0

        for i, char in enumerate(s):
            if char == "*":
                for j in range(26):
                    if lu[j]:
                        arr[lu[j].pop()] = "*"
                        break
            else:
                lu[ord(char) - 97].append(i)
        
        
        return "".join(char for char in arr if char != "*")