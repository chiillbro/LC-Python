class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_idx_s = {}
        char_idx_t = {}

        for i, char in enumerate(s):
            if char not in char_idx_s:
                char_idx_s[char] = i
            
            if t[i] not in char_idx_t:
                char_idx_t[t[i]] = i
            
            if char_idx_s[char] != char_idx_t[t[i]]:
                return False
        
        return True