class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # special triplet: 1st and 3rd should be same and twice the 2nd element

        # nums.sort()

        # seen = defaultdict(int)
        
        # count = 0

        # for num in nums:
        #     double = num * 2
        #     half = num / 2

        #     if seen[double] >= 2:
        #         count += 1
        #         seen[double] -= 2
        #     elif seen[half] >= 1 and seen[num] >= 1:
        #         count += 1
        #         seen[num] -= 1
        #         seen[half] -= 1
            
        #     else:
        #         seen[num] += 1
        
        # return count

        MOD = 10**9 + 7

        n = len(nums)

        freq, prev = Counter(nums), Counter()

        res = 0

        prev[nums[0]] = 1
        
        for i in range(1, n-1):
            x = nums[i]

            x2 = x << 1

            res = (res + (prev[x2] * (freq[x2] - prev[x2] - (x == 0)))) % MOD

            prev[nums[i]] += 1
        
        return res % MOD