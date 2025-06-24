class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # nums: int[]
        # key: int, k: int

        n = len(nums)

        key_indices = []

        for i, num in enumerate(nums):
            if num == key:
                key_indices.append(i)
    

        if not key_indices:
            return []
        
        res = []
        for idx in key_indices:
            start_idx = max(res[-1] + 1, idx - k) if res else max(idx - k, 0)
            end_idx = min(idx + k + 1, n)
            for i in range(start_idx, end_idx):
                res.append(i)

        return res