class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
    

    # ************** Approach 1: Using KMP (Knuth-Morris-Pratt) Method ***********#
    # TC: O(N + M), SC: O(M)

    #     lps = self._compute_lps(needle)

    #     return self._kmp_search(haystack, needle, lps)
    
    # def _compute_lps(self, pattern: str) -> List[int]:
    #     m = len(pattern)

    #     lps = [0] * m
    #     length = 0
    #     i = 1

    #     while i < m:
    #         if pattern[i] == pattern[length]:
    #             length += 1
    #             lps[i] = length
    #             i += 1
            
    #         else:
    #             if length != 0:
    #                 length = lps[length - 1]
    #             else:
    #                 lps[i] = 0
    #                 i += 1
        
    #     return lps
    
    # def _kmp_search(self, text: str, pattern: str, lps: List[int]) -> int:

    #     n, m = len(text), len(pattern)
    #     i = j = 0

    #     while i < n:
    #         if text[i] == pattern[j]:
    #             i += 1
    #             j += 1
            
    #         if j == m:
    #             return i - j
            
    #         if i < n and text[i] != pattern[j]:
    #             if j != 0:
    #                 j = lps[j-1]
    #             else:
    #                 i += 1
        
    #     return -1



    # ************** Approach 2: Using Rabin-Karp Method ***********#
    # Average: TC: O(N + M), Worst: O(N*M), SC: O(1)

        return self._rabin_karp(haystack, needle)
    
    def _rabin_karp(self, text: str, pattern: str) -> int:
        n, m = len(text), len(pattern)
        
        # Base 'd': A value representing the size of the alphabet or slightly larger.
        # Since we have lowercase English letters, 26 is the minimum size.
        # Using a small prime like 31 is common and often works well.
        d = 31  

        # Modulus 'q': A large prime number to prevent hash overflow and reduce collisions.
        # 10^9 + 7 is a common choice.
        q = 10**9 + 7 

         # Precompute d^(m-1) % q, where m = len(pattern). This is used for removing the leading char's contribution.
        # We can use pow(d, m - 1, q) for efficient modular exponentiation.
        h_factor = pow(d, m - 1, q)

        hash_b = 0  # Hash of the 'pattern'
        hash_window = 0 # Hash of the first window (m characters) in 'text'

        for i in range(m):
            hash_b = (d * hash_b + ord(pattern[i])) % q
            hash_window = (d * hash_window + ord(text[i])) % q
        

        for i in range(n - m + 1):
            if hash_b == hash_window:
                if text[i: i + m] == pattern:
                    return i
            

            if i < n - m:
                term1 = (ord(text[i]) * h_factor) % q
                hash_window = (hash_window - term1 + q) % q

                hash_window = (d * hash_window) % q

                term2 = ord(text[i+m])
                hash_window = (hash_window + term2) % q
        
        return -1
            


