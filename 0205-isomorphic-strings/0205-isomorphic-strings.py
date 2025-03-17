class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # char_idx_s = {}
        # char_idx_t = {}

        # for i, char in enumerate(s):
        #     if char not in char_idx_s:
        #         char_idx_s[char] = i
            
        #     if t[i] not in char_idx_t:
        #         char_idx_t[t[i]] = i
            
        #     if char_idx_s[char] != char_idx_t[t[i]]:
        #         return False
        
        # return True

        char_map = {}

        for sc, tc in zip(s,t):
            if sc in char_map:
                if char_map[sc] != tc:
                    return False
            
            elif tc in char_map.values():
                return False

            char_map[sc] = tc
        return True
        # return len(set(s)) == len(set(t)) == len(set(zip(s,t)))