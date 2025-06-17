class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # can be solved using sliding window and a set tracker

        track = defaultdict(int)
        left = 0

        ans = 0
        for right in range(len(s)):
            track[s[right]] += 1

            while len(track) < right - left + 1:
                track[s[left]] -= 1
                if not track[s[left]]:
                    del track[s[left]]
                left += 1

            ans = max(ans, len(track))
        

        return ans