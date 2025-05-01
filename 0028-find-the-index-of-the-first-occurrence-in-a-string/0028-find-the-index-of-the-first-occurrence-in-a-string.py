class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1

        if not needle:
            return 0
    

    # ************** Approach 1: Using KMP (Knuth-Morris-Pratt) Search Algorithm ***********#
    # TC: O(N + M), SC: O(M)

    #     lps = self._compute_lps(needle)

    #     return self._kmp_search(haystack, needle, lps)



    # ************** Approach 2: Using Rabin-Karp Algorithm ***********#
    # Average: TC: O(N + M), Worst: O(N*M), SC: O(1)

        # return self._rabin_karp(haystack, needle)


    


    # ************** Approach 3: Using Z-function Algorithm *********** #
    # TC: O(N + M), SC: O(N + M)

        n, m = len(haystack), len(needle)

        separator = "#"

        S = needle + separator + haystack
        len_s = len(S)

        z = self._compute_z_array(S)

        for i in range(m + 1, len_s):
            if z[i] == m:
                return i - (m + 1)
        
        return -1

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

        n, m = len(text), len(pattern)
        i = j = 0

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            
            if j == m:
                return i - j
            
            if i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        
        return -1
    
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
            # Calculate hash using polynomial rolling hash formula:
            # hash = (c1*d^(m-1) + c2*d^(m-2) + ... + cm*d^0) % q
            hash_b = (d * hash_b + ord(pattern[i])) % q
            hash_window = (d * hash_window + ord(text[i])) % q
        

        # --- Slide the Window and Compare Hashes ---
        for i in range(n - m + 1):
            # Check if current window's hash matches the pattern's hash
            if hash_b == hash_window:
                # Hash collision check: Verify character by character
                if text[i: i + m] == pattern:
                    return i
            

            # --- Calculate Hash for the Next Window (Rolling Hash) ---
            if i < n - m:
                # Remove leading character's contribution: T[i]
                term1 = (ord(text[i]) * h_factor) % q
                hash_window = (hash_window - term1 + q) % q # Add q to handle potential negative result

                # Shift the hash value to the left (multiply by base 'd')
                hash_window = (d * hash_window) % q

                # Add trailing character's contribution: T[i + len_b]
                term2 = ord(text[i+m])
                hash_window = (hash_window + term2) % q
        

        # --- No Match Found ---
        # If the loop finishes without finding a verified match
        return -1


    def _compute_z_array(self, s: str) -> List[int]:
        n = len(s)
        z = [0] * n

        left = right = 0

        for k in range(1, n):
            if k > right:
                left, right = k, k

                while right < n and s[right] == s[right - left]:
                    right += 1
                
                z[k] = right - left
                right -= 1
            else:
                
                k1 = k - left

                if z[k1] < right - k + 1:
                # if k + z[k1] <= right:
                    z[k] = z[k1] 
                else:
                    left = k
                    while right < n and s[right] == s[right - left]:
                        right += 1
                    
                    z[k] = right - left
                    right -= 1
        
        return z