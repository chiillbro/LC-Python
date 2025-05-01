class Solution:
    def shortestPalindrome(self, s: str) -> str:
        count = self._kmp_search(s[::-1], s)
        return s[count:][::-1] + s

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