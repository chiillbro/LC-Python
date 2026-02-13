class Solution:
    def longestBalanced(self, s: str) -> int:
        return max(self.mono(s), self.duo(s, "a", "b"), self.duo(s, "b", "c"), self.duo(s, "a", "c"), self.trio(s))


    def mono(self, s: str) -> int:
        max_cnt = 0
        cnt = 0
        prev_char = -1

        for i, char in enumerate(s):
            if prev_char == char:
                cnt += 1
            else:
                cnt = 1
                prev_char = char

            max_cnt = max(max_cnt, cnt)


        return max_cnt

    
    def duo(self, s: str, c1: str, c2: str) -> int:
        pos = {0: -1}
        max_cnt = 0
        delta = 0
        for i, char in enumerate(s):
            if char != c1 and char != c2:
                pos.clear()
                delta = 0
                pos[0] = i
            elif char == c1:
                delta += 1
            else:
                delta -= 1

            
            if delta in pos:
                max_cnt = max(max_cnt, i - pos[delta])
            else:
                pos[delta] = i
            

        return max_cnt

    
    def trio(self, s: str) -> int:
        pos = {(0, 0): -1}

        cnt0 = cnt1 = cnt2 = 0

        max_cnt = 0

        for i, char in enumerate(s):
            if char == "a":
                cnt0 += 1
            elif char == "b":
                cnt1 += 1
            else:
                cnt2 += 1
            
            key = (cnt1 - cnt0, cnt2 - cnt0)

            if key in pos:
                max_cnt = max(max_cnt, i - pos[key])
            else:
                pos[key] = i

        
        return max_cnt




