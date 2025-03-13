class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = len(arr)
        low, high = 0, N - 1

        while low <= high:
            mid = low + ((high - low) >> 1)

            if arr[mid] - (mid + 1) <  k:
                low = mid + 1
            else:
                high = mid - 1
        
        # return arr[high] +  (k - (arr[high] - (high + 1)))
        return k + high + 1