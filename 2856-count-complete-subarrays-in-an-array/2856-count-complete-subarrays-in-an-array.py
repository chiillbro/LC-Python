class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # counter = Counter(nums)
        # unique_len = len(counter.keys())

        # # for i, num in enumerate(nums):
        # i = 0
        # while len(counter.keys()) == unique_len and i < n:
        #     num = nums[i]
        #     counter[num] -= 1
        #     if counter[num] == 0:
        #         counter.pop(num)

        unique = len(set(nums))
        counter = defaultdict(int)
        res = right = 0

        for left in range(n):
            if left > 0:
                remove = nums[left-1]
                counter[remove] -= 1
                if not counter[remove]:
                    counter.pop(remove)
            
            while right < n and len(counter) < unique:
                add = nums[right]
                counter[add] += 1
                right += 1
            
            if len(counter) == unique:
                res += n - right + 1
            
        return res



        



