class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # nums: int[]
        # key: int, k: int

        n = len(nums)

        num_to_idx = defaultdict(list)

        for i, num in enumerate(nums):
            num_to_idx[num].append(i)
        

        if not key in num_to_idx:
            return []
        
        res = []
        for idx in num_to_idx[key]:
            start_idx = max(res[-1] + 1, idx - k) if res else max(idx - k, 0)
            end_idx = min(idx + k + 1, n)
            for i in range(start_idx, end_idx):
                res.append(i)

        # res = list(res)

        # res.sort()

        return res

