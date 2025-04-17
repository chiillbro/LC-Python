class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0

        # ** Simple enumeration - TC: O(n^2) ** #
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and not ((i * j) % k):
        #             res += 1


        # ** Optimal Approach: Using hashmap + GCD - TC: O(n * d(k)) ** #
        # here d(k) means no.of divisors of k (and is tiny when k <= 100)

        freq = defaultdict(lambda: defaultdict(int))

        for j, v in enumerate(nums):
            g_j = math.gcd(j, k)

            for g_i, count_i in freq[v].items():
                if (g_i * g_j) % k == 0:
                    res += count_i
            
            freq[v][g_j] += 1

        return res

# ** Observation via GCD **

# \U0001d456 ⋅ \U0001d457 ≡ 0 (mod \U0001d458) ⟺ gcd(\U0001d456,\U0001d458) × gcd(\U0001d457,\U0001d458) is a multiple of \U0001d458. 

# In our case we want (i⋅j) mod k = 0. If we let

#     \U0001d454\U0001d456 = gcd(\U0001d456,\U0001d458), \U0001d454\U0001d457 = gcd(\U0001d457,\U0001d458),
# then
#     i⋅j ≡ 0(mod k) ⟺ gi × gj ≡ 0 (modk)


# ** Algorithm **

# Keep a dictionary cnt that maps each g = gcd(idx, k) to “how many times we’ve seen an index with gcd = g so far, for this particular value of nums[i].”

# As you scan j from left to right:

# Compute g_j = gcd(j, k).

# For every entry (g_i, freq) in cnt, if (g_i*g_j) % k == 0, then all those freq indices i can pair with this j to form a valid (i,j). So add freq to your answer.

# Finally increment cnt[g_j] += 1.


# ** Complexity **

# You do \U0001d45b steps. At each step you iterate over at most d(k) distinct gcd‐values in the map, and d(k)≪k. So overall it’s O(nd(k)) plus the cost of a few GCDs.

# Since n≤100 and k≤100, you’re effectively O(100⋅d(100))≈O(1000), which is very fast.


# ** Why it works **

# We only compare indices i<j that have the same nums[i]==nums[j] because we group by v.

# Within that group, we use the gcd‐trick to check divisibility of i*j by k in O(d(k)).