class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0

        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and not ((i * j) % k):
        #             res += 1


        # ** Optimal Approach: Using GCD O(n * d(g)) ** #

        freq = defaultdict(lambda: defaultdict(int))

        for j, v in enumerate(nums):
            g_j = math.gcd(j, k)

            for g_i, count_i in freq[v].items():
                if (g_i * g_j) % k == 0:
                    res += count_i
            
            freq[v][g_j] += 1

        return res

