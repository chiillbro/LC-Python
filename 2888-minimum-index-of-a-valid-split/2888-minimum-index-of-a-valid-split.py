class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        count = Counter(nums)

        dominant = -1

        for key, val in count.items():
            if val << 1 > N:
                dominant = key
                break
        
        if dominant == -1:
            return -1
        
        left_count = 0
        right_count = count[dominant]

        for i in range(N-1):
            if nums[i] == dominant:
                left_count += 1
                right_count -=1

            if left_count << 1 > i+1 and right_count << 1 > N - i -1:
                return i
        
        return -1
    