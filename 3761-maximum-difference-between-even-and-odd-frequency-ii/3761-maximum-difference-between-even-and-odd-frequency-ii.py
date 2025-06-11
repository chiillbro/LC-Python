class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # s: string
        # k: integer
        # n = len(s)
        # # cnts = Counter(s)
        # prefix = [0] * n
        # prefix[0] = int()
        # for 

        # l = 0
        # for r in range(n):
            

        # return max(x for x in cnts.values() if (x & 1)) - min(x for x in cnts.values() if not (x & 1))

        n = len(s)

        def getStatus(cnt_a, cnt_b):
            return ((cnt_a & 1) << 1) | (cnt_b & 1)
        

        ans = float("-inf")

        for a in ['0', '1', '2', '3', '4']:
            for b in ['0', '1', '2', '3', '4']:
                if a == b:
                    continue
                
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0

                best = [float("inf")] * 4
                left = -1

                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b

                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = getStatus(prev_a, prev_b)

                        best[left_status] = min(best[left_status], prev_a - prev_b)

                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b

                    right_status = getStatus(cnt_a, cnt_b)

                    if best[right_status ^ 0b10] != float("inf"):
                        ans = max(ans, cnt_a - cnt_b - best[right_status ^ 0b10])


        return ans 