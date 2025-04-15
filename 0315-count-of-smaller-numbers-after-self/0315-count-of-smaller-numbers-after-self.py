class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)
    
    def update(self, index: int) -> None:
        # index += 1 # convert to 1-based index

        while index <= len(self.tree) - 1:
            self.tree[index] += 1
            index += index & -index
    
    def query(self, index: int) -> int:
        # index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        
        return res

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # def sort(indexed_nums):
        #     half = len(indexed_nums) // 2
        #     if half:
        #         left, right = sort(indexed_nums[:half]), sort(indexed_nums[half:])
        #         for i in range(len(enum))[::-1]:
        #             if not right or (left and left[-1][1] > right[-1][1]):
        #                 counts[left[-1][0]] += len(right)
        #                 indexed_nums[i] = left.pop()
        #             else:
        #                 indexed_nums[i] = right.pop()
        #     return indexed_nums

        # def merge_sort(arr):
        #     if len(arr) <= 1: return arr

        #     mid = len(arr) // 2
        #     left = merge_sort(arr[:mid])
        #     right = merge_sort(arr[mid:])
            
        #     merged = []
        #     i = j = 0

        #     while i < len(left) and j < len(right):
        #         if left[i][1] <= right[j][1]:
        #             counts[left[i][0]] += j
        #             merged.append(left[i])
        #             i += 1
        #         else:
        #             merged.append(right[j])
        #             j += 1
            
        #     while i < len(left):
        #         counts[left[i][0]] += j
        #         merged.append(left[i])
        #         i += 1
            
        #     merged.extend(right[j:])

        #     return merged


        # counts = [0] * len(nums)
        # indexed_nums = list(enumerate(nums))

        # merge_sort(indexed_nums)
        # return counts


        # ** Approach 3: Using Binary Indexed Tree(BIT) TC: O(n * logn), SC: O(n) **

        ans = [0] * len(nums)

        tree = FenwickTree(20000)
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = tree.query(nums[i] + 1_00_00)
            tree.update(nums[i] + 1_00_01)
        
        return ans