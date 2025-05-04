class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)

        track = defaultdict(list)
        res = 0

        for i, pair in enumerate(dominoes):
            pair.sort()
            pair = tuple(pair)
            if pair in track:
                res += len(track[pair])
            
            track[pair].append(i)
        
        return res