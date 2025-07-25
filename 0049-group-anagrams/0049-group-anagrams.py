class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anag = defaultdict(list)

        for s in strs:
            # key = ''.join(sorted(s))
            key = [0] * 26
            for c in s:
                key[ord(c) - 97] += 1
            group_anag[tuple(key)].append(s)
    
        return list(group_anag.values())