class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        n = len(words)
        
        freq = defaultdict(int)

        res = 0
        same_set = set()

        for word in words:
            rev = word[::-1]
            if rev in freq:
                res += 4
                freq[rev] -= 1
                if not freq[rev]:
                    freq.pop(rev)
            elif word == rev and word not in same_set:
                same_set.add(word)
            elif word == rev and word in same_set:
                res += 4
                same_set.remove(word)
            else:
                freq[word] += 1
        
        return res if not same_set else res + 2