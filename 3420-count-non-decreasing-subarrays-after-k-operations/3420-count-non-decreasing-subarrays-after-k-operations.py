class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = window_cost = 0
        right = n-1

        stack = deque()

        for left in range(n-1, -1, -1):
            newVal = nums[left]
            merged = 1

            while stack and stack[0][0] <= newVal:
                poppedValue, pastCount = stack.popleft()
                window_cost += (newVal - poppedValue) * pastCount
                merged += pastCount
            
            stack.appendleft([newVal, merged])

            while window_cost > k:
                window_cost -= stack[-1][0] - nums[right]
                if stack[-1][1] == 1:
                    stack.pop()
                else:
                    stack[-1][1] -= 1
                right -= 1
                
            ans += right - left + 1
        

        return ans