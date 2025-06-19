class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # nums: []int

        n = len(nums)

        stack = []
        total = 0

        # according to the problem statement, we need to find 
        # (max_val_k - min_val_k) for all the sub arrays of let's say size k

        # Now, we can write it as (sum of all max_vals) - (sum of all min_vals)
        # we need to find two partial sums as above and return the difference between max_vals and min_vals

        # sum of all the minimums
        for right in range(n+1): # looping till right == n to account for last element

            # either right should be n or the last element that was pushed onto the stack is no longer going to be the smallest element in the sub arrays formed with it
            # so clever way to accumulate all the score that the last element (nums[mid]) in the stack can make being the smallest for the sub arrays in the range left <-> right exclusively
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop() # the element idx that we need to account for at this point
                left = -1 if not stack else stack[-1]
                total -= nums[mid] * (mid - left) * (right - mid)

            stack.append(right)

        stack.clear()
        
        # same for the maximums
        for right in range(n+1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                
                total += nums[mid] * (mid - left) * (right - mid)
            
            stack.append(right)

        
        return total
