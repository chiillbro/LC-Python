class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        vowel_set = {'a', 'e', 'i', 'o', 'u'}

        freq_map = defaultdict(int)
        cons_count = low = high = res = 0

        for c in word:
            if c in vowel_set:
                freq_map[c] += 1
            else:
                cons_count += 1
            
            # **Shrink the window from the left** until we have at most k consonants.
            while cons_count > k:
                if word[high] in vowel_set:
                    freq_map[word[high]] -= 1
                    if freq_map[word[high]] == 0:
                        freq_map.pop(word[high])
                else:
                    cons_count -= 1
                
                high += 1
                low = high # reset the left boundary to hi
                
            # **Optionally extend the window** if it can be widened while preserving validity.
            while cons_count == k and high < N:
                if word[high] in vowel_set and freq_map[word[high]] > 1:
                    # If the next character is a vowel that appears more than once,
                    # we can remove one copy (virtually) and move hi.
                    freq_map[word[high]] -= 1
                    high += 1
                else:
                    break
            
            # If the current window has exactly k consonants and all vowels are present,
            # then every substring starting from index lo to hi (in a certain range) ending at hi is valid.
            if cons_count == k and len(freq_map) == 5:
                res += (high - low + 1)

        return res

        # ** Second Approach **

        # def atleast(k):
        #     vowel = defaultdict(int)
        #     res = non_vowel = l = 0
            
        #     for r in range(N):
        #         if word[r] in 'aeiou':
        #             vowel[word[r]] += 1
        #         else:
        #             non_vowel += 1
                
        #         while len(vowel) == 5 and non_vowel >= k:
        #             res += N - r
        #             if word[l] in 'aeiou':
        #                 vowel[word[l]] -= 1
        #                 if vowel[word[l]] == 0:
        #                     vowel.pop(word[l])
        #             else:
        #                 non_vowel -= 1
                    
        #             l += 1
        #     return res

        # return atleast(k) - atleast(k+1)