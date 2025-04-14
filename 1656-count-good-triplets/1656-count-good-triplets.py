class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    x, y, z = abs(arr[i] - arr[j]), abs(arr[j] - arr[k]), abs(arr[i] - arr[k])
                    if x <= a and y <= b and z <= c: res += 1
        
        return res