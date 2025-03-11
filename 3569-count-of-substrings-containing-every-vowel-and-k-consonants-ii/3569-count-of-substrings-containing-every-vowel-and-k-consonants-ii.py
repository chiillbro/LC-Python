class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        N = len(word)
        # vowel_set = {'a', 'e', 'i', 'o', 'u'}

        # freq_map = defaultdict(int)
        # cons_count = 0
        # left = res = 0

        # for right in range(N):
        #     char = word[right]
        #     freq_map[char] += 1
        #     if char not in vowel_set:
        #         cons_count += 1
            
        #     while cons_count > k:
        #         freq_map[word[left]] -= 1
        #         if word[left] not in vowel_set:
        #             cons_count -= 1
        #         left += 1
                
        #     if cons_count == k and all(freq_map[v] > 0 for v in vowel_set):
        #         temp = left
        #         char_map = [0] * 26
        #         while (temp <= right and 
        #             word[temp] in vowel_set and 
        #             (freq_map[word[temp]] + char_map[ord(word[temp]) - ord('a')])  > 1):
        #             char_map[ord(word[temp]) - ord('a')] += 1
        #             temp += 1
        #         res += (temp - left + 1)

        # return res

        def atleast(k):
            vowel = defaultdict(int)
            res = non_vowel = l = 0
            
            for r in range(N):
                if word[r] in 'aeiou':
                    vowel[word[r]] += 1
                else:
                    non_vowel += 1
                
                while len(vowel) == 5 and non_vowel >= k:
                    res += N - r
                    if word[l] in 'aeiou':
                        vowel[word[l]] -= 1
                        if vowel[word[l]] == 0:
                            vowel.pop(word[l])
                    else:
                        non_vowel -= 1
                    
                    l += 1
            return res

        return atleast(k) - atleast(k+1)