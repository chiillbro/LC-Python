class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(low, high):
            if low >= high:
                return 0
            
            count = 0
            mid = low + (high - low) // 2

            count += mergeSort(low, mid)
            count += mergeSort(mid + 1, high)
            count += self._countPairs(nums, low, mid, high)
            self._merge(nums, low, mid, high)

            return count

        return mergeSort(0, len(nums)-1)
    
    def _merge(self, nums, low, mid, high):
        left = low
        right = mid + 1
        merged = []

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                merged.append(nums[left])
                left += 1
            else:
                merged.append(nums[right])
                right += 1
            
        
        while left <= mid:
            merged.append(nums[left])
            left += 1
        
        while right <= high:
            merged.append(nums[right])
            right += 1
        
        for i in range(low, high + 1):
            nums[i] = merged[i - low]
    
    def _countPairs(self, nums, low, mid, high):
        count = 0
        right = mid + 1

        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            
            count += (right - (mid + 1))
        
        return count