class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        # count = Counter(nums)
        # for key, val in count.items():
        #     if val << 1 > N:
        #         dominant = key
        #         break
        
        # if dominant == -1:
        #     return -1

        # to optimize the solution further, there is little room for time complexity optimization, but we can optimize the space in which currently count dict is taking O(n) space, Instead of maintaining a counter to find the dominant element, we can use some thing like Boyer-Moore Mojority Voting Algorithm which finds the majority element in constant space
        candidate = None
        count = 0

        for num in nums:
            if not count:
                candidate = num
                count = 1
            
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        total = sum(1 for num in nums if num == candidate)
        if total << 1 <= N:
            return -1
        
        dominant = candidate
        
        left_count = 0
        right_count = total

        for i in range(N-1):
            if nums[i] == dominant:
                left_count += 1
                right_count -=1

            if left_count << 1 > i+1 and right_count << 1 > N - i -1:
                return i
        
        return -1
    