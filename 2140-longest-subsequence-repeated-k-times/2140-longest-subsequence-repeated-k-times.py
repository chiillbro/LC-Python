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
                # print("nxt", nxt)
                it = iter(s)

                # the below step does three things
                    # 1. for every character (ch) in nxt*k
                    # 2. the step "ch in it", the iterator "it" of s will scan for this ch, if
                        # found it will advance to next position of found position of ch for checking other characters which makes sense because we are checking for subsequence
                    # 3. if all of the characters found in a sequence, then append it to queue
                if all(ch in it for ch in nxt*k):
                    queue.append(nxt)

                # print("queue in loop", queue)
        
        return res