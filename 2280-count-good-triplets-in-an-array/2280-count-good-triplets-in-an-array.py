class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)
    

    def update(self, index: int, delta: int) -> None:
        index += 1

        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index: int) -> None:
        index += 1
        res = 0

        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res
        
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        pos2, reversedIdxMapping = [0] * n, [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        
        for i, num1 in enumerate(nums1):
            reversedIdxMapping[pos2[num1]] = i
        
        tree = FenwickTree(n)
        res = 0

        for value in range(n):
            pos = reversedIdxMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)

            res += left * right
        
        return res