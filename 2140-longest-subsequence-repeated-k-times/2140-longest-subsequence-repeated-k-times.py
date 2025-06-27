class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)

        candidate = sorted(
            [c for c, cnt in Counter(s).items() if cnt >= k], reverse=True
        )


        queue = deque(candidate)

        res = ""
        while queue:

            cur = queue.popleft()

            if len(cur) > len(res):
                res = cur
            
            for ch in candidate:
                nxt = cur + ch
                it = iter(s)

                if all(ch in it for ch in nxt*k):
                    queue.append(nxt)
        
        return res