class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        

        # ******* Approach 1: Using String Manipulation and checking ********** #
        # TC: O(N^2) worst case scenario, would be very slow for the given constraints


        # a = 'abcd', b = 'cdabcdab'
        # let's imagine the ways that we will be to create b by repeating a

        # Way 1.    b = k*a                   => (abcd)       ===> k
        # Way 2.1.  b = prefix + k*a          => cd (abcd)    ===> k + 1  \
        # Way 2.2.  b = k*a + suffix          => (abcd) ab    ===> k + 1  /
        # Way 3.    b = prefix + k*a + suffix => cd (abcd) ab ===> k + 2


         # --- Logic Analysis ---
        # Why check k_base, k_base + 1, and k_base + 2?

        # Minimum Length Requirement: For 'b' to be a substring of A_k (a repeated k times),
        # the length of A_k must be at least the length of b.
        # So, k * len(a) >= len(b)  =>  k >= len(b) / len(a).
        # Since k must be an integer, the smallest possible k is ceil(len(b) / len(a)).
        # Let k_min = ceil(len(b) / len(a)).

        # How does k_min relate to your k_base = floor(len(b) / len(a))?
        # - If len(b) is a multiple of len(a), then k_min = len(b) / len(a) = k_base.
        # - If len(b) is NOT a multiple of len(a), then k_min = floor(len(b) / len(a)) + 1 = k_base + 1.

        # Now, consider the string A_k. Where could 'b' possibly be found?
        # Imagine 'b' starts at index `s` within some A_k. It occupies indices `s` to `s + len(b) - 1`.
        # This occurrence might span across the boundary between concatenated 'a's.
        # Example: a = "abc", b = "cabca"
        # len_a = 3, len_b = 5. k_base = 5 // 3 = 1. k_min = ceil(5/3) = 2.
        # A_1 = "abc" (too short)
        # A_2 = "abcabc". Does it contain "cabca"? No.
        # A_3 = "abcabcabc". Does it contain "cabca"? Yes. Answer should be 3.
        # Your code checks k_base=1, k_base+1=2, k_base+2=3. It finds it at k=3.

        # Why is checking up to k_base + 2 enough?
        # Consider the string `S = a` repeated `k_min + 1` times.
        # Length(S) = (k_min + 1) * len(a).
        # Since k_min >= len(b) / len(a), we have k_min * len(a) >= len(b).
        # Therefore, Length(S) >= len(b) + len(a).
        # Any possible occurrence of `b` within an infinitely repeated `a` string (`a+a+a+...`) must fit within a window of length `len(b) + len(a) - 1`. Think about the maximum span: `b` could start at index 1 of one `a` and end at index `len(b)-1` within subsequent `a`'s, or start at index `len(a)-1` and finish later. The maximum span needed to guarantee seeing every possible substring of length `len(b)` is slightly less than `len(a) + len(b)`.
        # Since our string `S` (with `k_min + 1` repetitions) has length at least `len(b) + len(a)`, if `b` is *ever* going to be a substring of *any* `A_k`, it *must* be a substring of `S = A_{k_min + 1}`.

        # So, we only need to check `A_{k_min}` and `A_{k_min + 1}`.
        # - Case 1: `len(b)` is multiple of `len(a)`. `k_min = k_base`. We check `A_{k_base}` and `A_{k_base + 1}`.
        # - Case 2: `len(b)` is not multiple of `len(a)`. `k_min = k_base + 1`. We check `A_{k_base + 1}` and `A_{k_base + 2}`.

        # The code checks `A_{k_base}`, `A_{k_base + 1}`, and `A_{k_base + 2}`. This covers both cases correctly. It might do one unnecessary check in Case 1 (checking `k_base + 2`), but it's guaranteed to find the correct minimum `k` if it exists within these checks.

        # k = len_b // len_a

        # checking for Way 1
        # ka = a * k # Create string A_{k_base}
        # if b in ka:
        #     return k
        
        # checking for Way 2
        # ka += a # Append 'a' once more to create A_{k_base + 1}
        # if b in ka:
        #     return k + 1
        
        # checking for Way 3
        # ka += a # Append 'a' again to create A_{k_base + 2}
        # if b in ka:
        #     return k + 2
        
        # If b wasn't found in any of the candidate strings up to A_{k_base + 2}
        # (which covers A_{k_min} and A_{k_min + 1}), it can never be a substring.
        # return -1

         # --- Efficiency ---
        # String Concatenation: `a * k` takes O(k * len(a)) time. The longest string `ka` has length roughly `len(b) + 2*len(a)`.
        # Substring Search: `b in ka`. Python's `in` is optimized (often using algorithms like Boyer-Moore or variations), but its worst-case time complexity can be O(len(ka) * len(b)).
        # Total worst-case complexity: Roughly O((len(b) + len(a)) * len(b)). If len(a) and len(b) are ~N, this is O(N^2).
        # This can be too slow if N is large (like 10^4).







        # ********** Approach 2: Using KMP (Knuth-Morris-Pratt) Algorithm ********** #
        # TC: O(len(a) + len(b)) - linear time, very Optimal


        k_base = (len_b + len_a - 1) // len_a

        max_reps_to_check = k_base + 1

        T = a * max_reps_to_check

        # lps = self._compute_lps(b)
        
        # match_index = self._kmp_search(T, b, lps)

        # if match_index == -1:
        #     return -1
        
        # else:
        #     required_idx = (match_index + len_b + len_a - 1) // len_a

        #     return required_idx


        # ********** Approach 3: Using Rabin-Karp Algorithm ********** #
        # TC: Average Case: O(len(a) + len(b)), Worst Case: O(len(a) * len(b)), SC: O(1)
        
        match_idx =  self._rabin_karp(T, b)

        if match_idx != -1:
            required_idx = (match_idx + len_b + len_a - 1) // len_a

            return required_idx
        
        return -1

    
    def _rabin_karp(self, text: str, pattern: str) -> int:
        n, m = len(text), len(pattern)
        # A value representing the size of the alphabet or slightly larger
        d = 31
        
        # A large prime number to prevent hash overflow and reduce collisions
        q = 10**9 + 7

        # used later for removing the leading char's contribution
        h_factor = pow(d, m-1, q) # in Integer math, this equals to (d^len_b) % q

        h_base = 0 # hash of the pattern
        h_window = 0 # hash of the first window of text of m characters


        for i in range(m):
            h_base = (d * h_base + ord(pattern[i])) % q
            h_window = (d * h_window + ord(text[i])) % q
        

        for i in range(n - m + 1):
            if h_base == h_window:
                if text[i: i+m] == pattern:
                    return i
            
            if i < n - m:
                term1 = (ord(text[i]) * h_factor) % q

                h_window = (h_window - term1 + q) % q
                h_window = (h_window * d) % q

                term2 = ord(text[i+m])
                h_window = (h_window + term2) % q
        

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
                    length = lps[length-1]
                
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
            



