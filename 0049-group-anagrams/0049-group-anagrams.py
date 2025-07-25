class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anag = defaultdict(list)

        for s in strs:
            # key = ''.join(sorted(s)) # O K logK

            key = [0] * 26 # O(K), this is efficient if the word length is in 1000s or more and can get you a brownie point in interviews if mentioned
            for c in s:
                key[ord(c) - 97] += 1
            group_anag[tuple(key)].append(s)
    
        return list(group_anag.values())