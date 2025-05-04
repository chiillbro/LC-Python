class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)

        track = defaultdict(int)
        res = 0

        for i, pair in enumerate(dominoes):
            pair = tuple(sorted(pair))
            if pair in track:
                res += track[pair]
            
            track[pair] += 1
        
        return res