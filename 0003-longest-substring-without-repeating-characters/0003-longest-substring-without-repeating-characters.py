class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = res = 0

        # counter = defaultdict(int)

        # for right in range(n):
        #     counter[s[right]] += 1
        #     # if right > 0:
        #     while left <= right and len(counter) < (right - left + 1):
        #         counter[s[left]] -= 1
        #         if not counter[s[left]]:
        #             counter.pop(s[left])
        #         left += 1
            
        #     res = max(res, right - left + 1)
        

        # More Cleaner and Direct approach using a Set

        # unique = set()

        # for right in range(n):
        #     while s[right] in unique:
        #         unique.remove(s[left])
        #         left += 1
            
        #     unique.add(s[right])

        #     res = max(res, right - left + 1)

        char_mask = [-1] * 256

        for right in range(n):
            if char_mask[ord(s[right])] != -1:
                left = max(char_mask[ord(s[right])] + 1, left)
            
            char_mask[ord(s[right])] = right

            res = max(res, right - left + 1)
            
        return res