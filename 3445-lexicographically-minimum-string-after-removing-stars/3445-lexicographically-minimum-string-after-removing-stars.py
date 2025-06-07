class Solution:
    def clearStars(self, s: str) -> str:
        
        # Approach 1- Greedy: TC: O(N * 26), SC: O(N + 26)
        # lu = defaultdict(list)
        # # lu = [[] for _ in range(26)]
        # arr = list(s)

        # # has_star = 0

        # for i, char in enumerate(s):
        #     if char == "*":
        #         for j in range(26):
        #             if lu[j]:
        #                 arr[lu[j].pop()] = "*"
        #                 break
        #     else:
        #         lu[ord(char) - 97].append(i)
        
        
        # return "".join(char for char in arr if char != "*")

        # Approach 2 - Using Priority Queue, TC: O(N * log N), SC: O(N)

        heap = []

        s_arr = list(s)

        for i, char in enumerate(s):
            if char != "*":
                heappush(heap, (char, -i))
            
            else:
                _, j = heappop(heap)
                s_arr[-j] = ''
                s_arr[i] = ''
        

        return ''.join(s_arr)