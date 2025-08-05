class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [0] * n
        
        not_placed = 0
        for fruit in fruits:
            for i in range(n):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = 1
                    break
            else: not_placed += 1

        
        return not_placed