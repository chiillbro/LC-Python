class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        left = 0

        t_counts = Counter(t)

        t_counts_len = len(t_counts)
        start, end = -1, inf

        s_counts = defaultdict(int)
        
        match_count = 0
        for right in range(n):
            s_counts[s[right]] += 1
            
            if s[right] in t_counts and s_counts[s[right]] == t_counts[s[right]]: 
                match_count += 1

            # elif s_counts[s[right]] == t_counts[s[right]] + 1:
            #     match_count -= 1
            
            # if match_count == t_counts_len:
            #     if right - left + 1 < end - start:
            #         start, end = left, right
            while match_count == t_counts_len and left <= right:
                if right - left < end - start:
                    start, end = left, right

                if s[left] in t_counts and s_counts[s[left]] == t_counts[s[left]]:
                    match_count -= 1
                # elif s_counts[s[left]] == t_counts[s[left]] - 1:
                #     match_count -= 1

                s_counts[s[left]] -= 1
                
                left += 1
        

        if start == -1: return ""

        return s[start:end+1]



