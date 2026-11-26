class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        def feasible(L: int):
            # double hashing to eliminate the collisions on adversarial test cases
            B1, B2 = 10^5 + 3, 10^5 + 19
            M1, M2 = 10**9 + 7, 10**9 + 0

            highest_power_1, highest_power_2 = pow(B1, L-1, M1), pow(B2, L-1, M2)

            hashes = {}
            current_hash_1 = current_hash_2 = 0
            for i in range(L):
                current_hash_1 = (current_hash_1 * B1 + nums[i]) % M1
                current_hash_2 = (current_hash_2 * B2 + nums[i]) % M2
            
            hashes[(current_hash_1, current_hash_2)] = 1

            for i in range(L, n):
                leaving = nums[i-L]
                incoming = nums[i]

                current_hash_1 = (current_hash_1 - leaving * highest_power_1) % M1
                current_hash_1 = (current_hash_1 * B1 + incoming) % M1
                
                current_hash_2 = (current_hash_2 - leaving * highest_power_2) % M2
                current_hash_2 = (current_hash_2 * B2 + incoming) % M2

                hashes[(current_hash_1, current_hash_2)] = hashes.get((current_hash_1, current_hash_2), 0) + 1

            
            return any(c == 1 for c in hashes.values())
        
        low, high = 1, n

        while low < high:
            mid = (low + high) // 2

            if feasible(mid):
                high = mid
            
            else:
                low = mid + 1
        
        return high
