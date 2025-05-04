class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # count = self._kmp_search(s[::-1], s)
        # return s[count:][::-1] + s

        return self.shortestPalindrome_KMP(s)
    
    def shortestPalindrome_KMP(self, s: str) -> str:
        if not s:
            return s
        
        s_rev = s[::-1]

        temp = s + "#" + s_rev

        lps = self._compute_lps(temp)

        k = lps[-1]

        suffix_to_reverse = s[k:]
        prefix_to_add = suffix_to_reverse[::-1]

        return prefix_to_add + s
    
    def _compute_lps(self, pattern: str) -> List[int]:
        m = len(pattern)

        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps


    def _kmp_search(self, text: str, pattern: str) -> int:
        final_str = pattern + "#" + text

        lps = [0] * len(final_str)
        length = 0
        i = 1

        while i < len(final_str):
            if final_str[i] == final_str[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length > 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps[-1]