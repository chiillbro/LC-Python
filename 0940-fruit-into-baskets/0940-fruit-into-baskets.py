class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)

        freq = defaultdict(int)

        left = res = 0

        for right in range(n):
            freq[fruits[right]] += 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    freq.pop(fruits[left])
                left += 1
            
            if len(freq) <= 2:
                res = max(res, right - left + 1)
            
        
        return res
            
