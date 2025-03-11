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
            
            while cons_count > k:
                if word[high] in vowel_set:
                    freq_map[word[high]] -= 1
                    if freq_map[word[high]] == 0:
                        freq_map.pop(word[high])
                else:
                    cons_count -= 1
                
                high += 1
                low = high
                
            while cons_count == k and high < N:
                if word[high] in vowel_set and freq_map[word[high]] > 1:
                    freq_map[word[high]] -= 1
                    high += 1
                else:
                    break
            
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