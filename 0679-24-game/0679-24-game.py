class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # cards: int[...4], each element is in the range 1 to 9
        THRESHOLD = 10**(-1)

        def backtrack(cur):
            if len(cur) == 1:
                return abs(cur[0] - 24) < THRESHOLD
            
            n = len(cur)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue

                    rem = [cur[k] for k in range(n) if k != i and k != j]
                    a, b = cur[i], cur[j]
                    candidates = [a+b, a-b, b-a, a*b]
                    
                    if b > THRESHOLD:
                        candidates.append(a/b)

                    
                    if a > THRESHOLD:
                        candidates.append(b/a)

                    for candidate in candidates:
                        if backtrack(rem + [candidate]):
                            return True

            return False
        


        return backtrack(cards)