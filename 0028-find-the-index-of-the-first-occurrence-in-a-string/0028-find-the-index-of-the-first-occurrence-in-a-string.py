class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1

        lps = self._compute_lps(needle)

        return self._kmp_search(haystack, needle, lps)
    
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
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    def _kmp_search(self, text: str, pattern: str, lps: List[int]) -> int:

        m, n = len(text), len(pattern)
        i = j = 0

        while i < m:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            
            if j == n:
                return i - j
            
            if i < m and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        
        return -1
