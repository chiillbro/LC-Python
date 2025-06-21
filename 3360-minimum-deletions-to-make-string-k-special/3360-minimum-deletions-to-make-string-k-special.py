class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # word: string
        # k: int

        freq = Counter(word)

        # min_freq = min(freq.values())

        # max_freq = abs(k - min_freq)

        freqs_arr = freq.values()

        # freqs_arr.sort()
        # if freqs_arr[-1] - freqs_arr[0] <= k:
        #     return 0

        res = len(word)
        for a in freqs_arr:
            deleted = 0
            for b in freqs_arr:
                if a > b:
                    deleted += b
                elif b - k > a:
                    deleted += b - (a + k)
            
            res = min(res, deleted)
        
        return res


