class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # if len(basket2) > len(basket1):
        #     return minCost(basket2, basket1)

        # counts1 = Counter(basket1)
        # counts2 = Counter(basket2)

        # for cost, cnt in counts1:
        #     if cnt & 1:
        #         if cost not in counts2 or (counts2[cost] & 1) == 0:
        #             return -1
        #     else:
        #         if cost in counts2 and counts2[cost] & 1:
        #             return -1
        # baskets1.sort(); baskets2.sort()

        freq = Counter()

        m = math.inf
        for c in basket1:
            freq[c] += 1
            m = min(m, c)
        
        for c in basket2:
            freq[c] -= 1
            m = min(m, c)
        
        merge = []

        for c, v in freq.items():
            if abs(v) % 2 != 0:
                return -1
            
            merge.extend([c] * (abs(v) // 2))


        if not merge:
            return 0
        
        merge.sort()
        return sum(min(2*m, x) for x in merge[:len(merge)//2])


