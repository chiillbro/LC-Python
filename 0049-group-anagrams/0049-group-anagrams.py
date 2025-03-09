class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # sorted_word = tuple(sorted(word))
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1

            anagrams[tuple(key)].append(word)
        return list(anagrams.values())

