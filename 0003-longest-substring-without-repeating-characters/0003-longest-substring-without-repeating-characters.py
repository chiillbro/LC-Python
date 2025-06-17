class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # can be solved using sliding window and a dict or a set

        # Approach 1

        # track = defaultdict(int)
        # left = 0

        # ans = 0
        # for right in range(len(s)):
        #     track[s[right]] += 1

        #     while len(track) < right - left + 1:
        #         track[s[left]] -= 1
        #         if not track[s[left]]:
        #             del track[s[left]]
        #         left += 1

        #     ans = max(ans, len(track))
        

        # return ans


        # Approach 2
        
        # track = set()
        # left = 0

        # ans = 0

        # for right in range(len(s)):
        #     while s[right] in track:
        #         track.remove(s[left])
        #         left += 1
            
        #     track.add(s[right])

        #     ans = max(ans, len(track))

        # return ans


        # Approach 3
        char_mask = [-1] * 256
        left = 0

        ans = 0

        for right in range(len(s)):
            if char_mask[ord(s[right])] != -1:
                left = max(left, char_mask[ord(s[right])] + 1)
            
            char_mask[ord(s[right])] = right

            ans = max(ans, right - left + 1)
        
        return ans