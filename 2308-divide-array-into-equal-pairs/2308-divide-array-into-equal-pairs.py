class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        N = len(nums)
        pairs = 0
        # count = Counter(nums)

        # return len(count) == pair_len and all(val == 2 for num, val in count.items())

        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] == 2:
                pairs += 1
                count.pop(num)
        
        if len(count) == 0 and (pairs) == (N >> 1):
            return True

        return False
