class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # n = len(words)
        
        # freq = defaultdict(int)
        # res = 0
        # same_word_set = set() # can be solved without using set, but let's use our options

        # for word in words:
        #     rev = word[::-1]
        #     if rev in freq:
        #         res += 4
        #         freq[rev] -= 1
        #         if not freq[rev]:
        #             freq.pop(rev)
        #     elif word == rev and word not in same_word_set:
        #         same_word_set.add(word)
        #     elif word == rev and word in same_word_set:
        #         res += 4
        #         same_word_set.remove(word)
        #     else:
        #         freq[word] += 1
        
        # return res if not same_word_set else res + 2





        # Approach 2: Clever

        counts = Counter(words)
        center = 0
        res = 0

        for word in counts.keys():
            rev = word[::-1]

            if word == rev:
                res += 2*(counts[word]//2)
                if counts[word] & 1:
                    center = 1
            
            elif rev < word:
                res += 2*min(counts[rev], counts[word])
        
        return (res + (1 if center else 0))*2