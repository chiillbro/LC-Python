class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        count = 0

        # for i in range(N):
        #     current_window = [colors[(i + j) % N] for j in range(k)]

        #     is_alternating = True
        #     for j in range(1, k - 1):
        #         if current_window[j] == current_window[j-1] or current_window[j] == current_window[j+1]:
        #             is_alternating = False
        #             break
            
        #     if is_alternating:
        #         count += 1

        # return count

        # alt = [0] * N

        # for i in range(N):
        #     alt[i] = 1 if colors[i] != colors[(i+1)%N] else 0
        
        # prefix = [0] * (N + k + 1)

        # for i in range(N + k):
        #     prefix[i+1] = prefix[i] + alt[i % N]
        
        # for i in range(N):
        #     s = prefix[i + k - 1] - prefix[i]

        #     if s == k-1:
        #         count += 1

        l = []

        for i in range(N-1):
            if colors[i] == colors[i+1]:
                l.append(i)
        
        if colors[N-1] == colors[0]:
            l.append(N-1)
        if len(l) == 0:
            return N
        
        l.append(l[0] + N)

        for i in range(len(l) - 1):
            count += max(0, l[i+1] - l[i] - k + 1)
        
        return count