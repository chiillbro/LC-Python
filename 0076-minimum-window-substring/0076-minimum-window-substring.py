class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Approach 1 using two for loops, O(N ^ 2) results in TLE
        n, m = len(s), len(t)

        if n < m:
            return ""
        
        start, min_wind = -1, float('inf')

        # for i in range(n):
        #     freq_map, count = Counter(t), 0
        #     for j in range(i, n):
        #         if freq_map[s[j]] > 0: count += 1

        #         freq_map[s[j]] -= 1

        #         if count == m and j - i + 1 < min_wind:
        #             min_wind = j - i + 1
        #             start = i
        #             break
        

        # return s[start:start + min_wind] if min_wind != float("inf") else ""


        # Optimal Solution using Sliding Window
        
        count = 0
        freq_map = Counter(t)
        
        left = 0

        for right in range(n):
            if freq_map[s[right]] > 0: count += 1

            freq_map[s[right]] -= 1

            while count == m:
                if right - left + 1 < min_wind:
                    min_wind = right - left + 1
                    start = left
                
                freq_map[s[left]] += 1
                if freq_map[s[left]] > 0: count -= 1
                left += 1
        
        return "" if start == -1 else s[start:start + min_wind]

        
