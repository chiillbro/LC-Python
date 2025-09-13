class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels_freq = defaultdict(int)
        cons_freq = defaultdict(int)

        vowels = {"a", "e", "i", "o", "u"}
        max_vowel_freq = max_cons_freq = 0

        for c in s:
            if c in vowels:
                vowels_freq[c] += 1
                max_vowel_freq = max(max_vowel_freq, vowels_freq[c])
            else:
                cons_freq[c] += 1
                max_cons_freq = max(max_cons_freq, cons_freq[c])

        
        return max_vowel_freq + max_cons_freq