class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        track = defaultdict(int)
        left = considerCharCount = res = 0

        for right in range(n):
            track[s[right]] += 1
            considerCharCount = max(track[s[right]], considerCharCount)
            if right - left + 1 - considerCharCount > k:
                track[s[left]] -= 1
                if not track[s[left]]:
                    track.pop(s[left])
                left += 1

            res = max(res, right - left + 1)
        
        return res