class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10_00_00_00_00 + 7
        n = len(nums)
        prime_scores = []

        for i, num in enumerate(nums):
            cur = 0
            if not num & 1:
                cur += 1
            
            while not num & 1:
                num >>= 1
            
            for factor in range(3, int(math.sqrt(num)) + 1, 2):
                if num % factor == 0:
                    cur += 1
                    while num % factor == 0:
                        num //= factor
            if num > 2:
                cur += 1
            prime_scores.append(cur)
        
        prev_dominant = [-1] * n
        next_dominant = [n] * n

        decreasing_prime_score_stack = [] # monotonic stack
        for index in range(n):
            while (
                decreasing_prime_score_stack
                and prime_scores[decreasing_prime_score_stack[-1]] < prime_scores[index]
            ):
                top_index = decreasing_prime_score_stack.pop()

                next_dominant[top_index] = index
            
            if decreasing_prime_score_stack:
                prev_dominant[index] = decreasing_prime_score_stack[-1]
            
            decreasing_prime_score_stack.append(index)
        
        processing_queue = []

        for i, num in enumerate(nums):
            heappush(processing_queue, (-num, i))
        
        def _power(base, exponent):
            res = 1

            while exponent != 0:
                if exponent & 1:
                    res = (res * base) % MOD
                
                base = (base * base) % MOD
                exponent >>= 1
            return res
        
        score = 1
        while k > 0:
            num, index = heappop(processing_queue)
            num = -num

            sub_arrays_count = (next_dominant[index] - index) * (index - prev_dominant[index])
            operations = min(k, sub_arrays_count)
            score =  (score * _power(num, operations)) % MOD
            k -= operations

        return score % MOD