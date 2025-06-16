class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # n = len(ring)
        # char_to_indices = defaultdict(list)

        # for i, char in enumerate(ring):
        #     chat_to_indices[char].append(i)
        
        # steps = len(key)

        # cur_first, cur_last = 0, n
        # for char in key:
        #     relevant_indices = char_to_indices[char]

        #     idx = None
        #     if len(relevant_indices) > 1:
        #         first = relevant_indices[0]
        #         last = relevant_indices[-1]

        #         dist1 = first - cur_first
        #         dist2 = cur_last - last

        #         if dist1 < dist2:
        #             idx = first
        #         else:
        #             idx = last
        #     else:
        #         idx = relevant_indices[0]


        # Serously bro, this is not how you approach Hard level problems you dumb fuck
        # Remember, Hard level problems cannot just be solved with control statements, you have to use algorithms you fucker

        # first let's solve this using Top-Down Dynamic Programming and later focus on to get Bottom-up one

        n, m = len(ring), len(key)

        def countSteps(cur: int, next: int) -> int:
            steps_between = abs(cur - next)
            steps_around = n - steps_between

            return min(steps_between, steps_around)
        

        memo = {}
        def dfs(ring_idx, key_idx, min_steps):
            mem_key = ring_idx, key_idx, min_steps

            if mem_key in memo:
                return memo[mem_key]
            if key_idx == m:
                return 0
            

            for i in range(n):
                if ring[i] == key[key_idx]:
                    total_steps = countSteps(ring_idx, i) + 1 + \
                                        dfs(i, key_idx + 1, inf)
                    
                    min_steps = min(min_steps, total_steps)

            memo[mem_key] = min_steps 
            return min_steps
            
        

        return dfs(0, 0, inf)
            

